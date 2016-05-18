/*
   WORD CLOCK - 8x8 For use with Tempus Fugit board
   By David Saul https://meanderingpi.wordpress.com/

   Release Version 1 - previuos development version  = rev 6 
   

   Inspired by the work of Andy Doro - NeoPixel WordClock from the Adafruit website

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
   HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
   OTHER DEALINGS IN THE SOFTWARE.

   Software:
   This code requires the following external libraries:
   - RTClib https://github.com/adafruit/RTClib
   - LedControl https://github.com/wayoda/LedControl/releases

   Wiring:
   This code is designed to work with the Tempus Fugit board - a simple wordclock for Arduino and the PiZero
   - add Github ref in here

   grid pattern

    H A T W E N T Y
    F I F V T E E N
    L F * P A S T O
    N I N E I G H T
    O N E T H R E E
    T W E L E V E N
    F O U R F I V E
    S I X S E V E N
*/

// include the library code:
#include <Wire.h>
#include <RTClib.h>
#include <LedControl.h>
#include <EEPROM.h>

/*
  Define pins
  Buttons
  Button1 - D9  [select]
  Button2 - D8  [up]
  Button3 - D7  [down]


  Max7219
  pin 12 is connected to the DataIn
  pin 11 is connected to the CLK
  pin 10 is connected to LOAD
  We have only a single MAX72XX.

*/

LedControl lc = LedControl(12, 11, 10, 1);

RTC_DS1307 RTC; // Establish clock object
DateTime theTime; // Holds current clock time


// setup button and LED addresses

const int button1 = 9;
const int button2 = 8;
const int button3 = 7;

const int ledPin = 13;      // use for seconds indicator

// setup for LDR connection
const int analogInPin = A7;  // Analog input connected to LDR
//const int analogOutPin = 3; // Analog output pin that the LED is attached to  - for debug only
const int LDR_drv = 2;        // +5v drive for LDR - this is needed for compatability with Pi Zero circuit


//EEPROM memory allocations
const int wr_no0 = 0;
const int wr_no1 = 1;
const int wr_no2 = 2;
const int wr_no3 = 3;

const int brlim_add = 4; // EEPROM address for stored bright lim figure

int bright = 0;   // global variable for Max7219 brightness
int raw_bright = 0; // raw LDR value
int raw_bright_old = 1023; // old raw value used for averaging
int uncor = 0;
int c_flag = false;
int bright_lim = 15;  // brightness range limiting variable

// working hour and minute global variables
int min_x = 0;
int hour_x = 0;


void setup() {
  // Setup code

  //Serial for debugging
  Serial.begin(9600);

  Serial.println("Tempus Fugit WordClock Application ENGLISH Version");
  Serial.println("Initialiing....");
  Serial.println();



  // initialize the pushbutton pins as an inputs:
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);

  // initialize the board LED pin as an output - for seconds indicator
  pinMode(ledPin, OUTPUT);

  // initialze LDR +5 drive
  pinMode(LDR_drv, OUTPUT);    // this is the LDR drive voltage
  digitalWrite(LDR_drv, HIGH);

  //pinMode(3,OUTPUT);    // for debug connect LED to D3 to check operation

  /*
    Setup the MX7219
    The MAX7219 is in power-saving mode on startup we have to do a wakeup call
  */
  lc.shutdown(0, false);
  /* Set the brightness to a max values - for green display */
  lc.setIntensity(0, 15);
  /* and clear the display */
  lc.clearDisplay(0);

  // start clock
  Wire.begin();  // Begin I2C
  RTC.begin();   // begin clock


  if (! RTC.isrunning()) {
    Serial.println("RTC is NOT running!");
    Serial.println("will set RTC to original compile time");
    // display Error message on display
    lc.setColumn(0, 2, B00101010); // display E E E
    delay(1000);

    // following line sets the RTC to the date & time this sketch was compiled
    RTC.adjust(DateTime(__DATE__, __TIME__));
    Serial.println("RTC Time set");
  }

  // display INT for 1 second
  // this is the window to force a RTC time reset
  lc.setColumn(0, 4, B01101001); // display INIT
  delay(1500);

  // If buttons 2 & 3 held down at power up for approx 5 seconds
  // attempt to set clock to original compile time
  if (digitalRead(button2) == LOW && digitalRead(button3) == LOW) {
    int count = 0;
    lc.clearDisplay(0);   // clear display
    // wait until the 2 buttons have been held for approx 5 seconds
    // before reseting the time
    // display diagnol line
    for (count = 0; count < 8; count++)
    {
      lc.setRow(0, count, 1 << count);
      delay(500);
      if (digitalRead(button2) == HIGH || digitalRead(button3) == HIGH) {
        Serial.println("RTC update ABORTED");
        Serial.println();
        count = 9999;     // force count to invalid number
      }
    }
    // if button held down for complete time update RTC
    if (count == 8) {
      RTC.adjust(DateTime(__DATE__, __TIME__));
      Serial.println("RTC Time reset to complile time");
      lc.clearDisplay(0);   // clear display
      // wait for buttons to be released
      while (digitalRead(button2) == LOW || digitalRead(button3) == LOW)
      {
        delay(20);
      }

    }
  }



  // Display startup sequence

  bright_lim = EEPROM.read(brlim_add);
  Serial.print("Stored bright limit value = ");
  Serial.println(bright_lim);
  if (bright_lim > 14)     // check to if EEPROM has been written prviously
  {
    bright_lim = 15;       // if not force to 15
  }
  adjustBrightness();   // set initial display brightness

  st_display();// display rollig screen 
  Serial.println("Initialisation complete, clock running");
  Serial.println();
  Serial.println();

}


void loop() {
  // Main Clock code:

  int count = 0;      // setup temp count variable

  // get time from the RTC
  DateTime theTime = RTC.now();
  // theTime = calculateTime(); // takes into account DST   - comment out until sorted out

  // save time as simple variable
  min_x = theTime.minute();
  hour_x = theTime.hour();

  // serial print theTime variable - for debug

  Serial.print(theTime.year(), DEC);
  Serial.print('/');
  Serial.print(theTime.month(), DEC);
  Serial.print('/');
  Serial.print(theTime.day(), DEC);
  Serial.print(' ');
  Serial.print(theTime.hour(), DEC);
  Serial.print(':');
  Serial.print(theTime.minute(), DEC);
  Serial.print(':');
  Serial.print(theTime.second(), DEC);
  Serial.print(' ');

  // Update time display
  displayTime();

  // output LDR info - for degbug only
  Serial.print("Raw = ");
  Serial.print(raw_bright);
  Serial.print(" Corrected Max =  ");
  Serial.print(bright);
  Serial.print(" bright_lim = ");
  Serial.println(bright_lim);

  // check bright_lim var needs to be updated in EEPROM
  update_EEPROM();

  Serial.println();   // - for debug only

  // key check  & general delay loop, setup to give display update time of about once every 2 minutes
  while (count < 1200)  // setup for 2 min delay
  {
    count++;
    delay(100);
    // check the state of the button1 [select]
    if (digitalRead(button1) == LOW) {
      while (digitalRead(button1) == LOW) // wait for key to be released
      {
        delay(20);
      }
      // valid select button press detected - jump to keypress
      keypress();
      count = 2000;    // force immediate display update
    }

    /*
        The following section of code allows you the set a range variable between 1 & 15
        This is used to limit the bightness of the display
        15 = no limit full 7219 brightness setting range available
        1 = Max 7219 brighness will be limited to 0 or 1 [depending on ambient brighness]
        5 = Max 7219 brighness will be limited to 0 or 5 [depending on ambient brighness]
    */


    // check the state of the button 3 [inc display limit range]
    if (digitalRead(button3) == LOW) {
      while (digitalRead(button3) == LOW) // wait for key to be released
      {
        delay(20);
      }
      bright_lim++;
      if (bright_lim > 15) {
        bright_lim = 15;
        lc.setLed(0, 0, 7, true);     // flash H
        delay(250);
        lc.setLed(0, 0, 7, false);
      }
      lc.setLed(0, 2, 5, true);     // flash * with to indicate every push or S2 or S3
      delay(250);
      lc.setLed(0, 2, 5, false);


      // update display brighness
      adjustBrightness();

      //for debug only
      Serial.print("Range = ");
      Serial.println(bright_lim);
    }

    // check the state of the button 2 [dec display limit range]
    if (digitalRead(button2) == LOW) {
      while (digitalRead(button2) == LOW) // wait for key to be released
      {
        delay(20);
      }
      bright_lim--;
      if (bright_lim < 1) {
        bright_lim = 1;
        lc.setLed(0, 0, 5, true);     // flash H
        delay(250);
        lc.setLed(0, 0, 5, false);
      }
      lc.setLed(0, 2, 5, true);     // flash * with to indicate every push or S2 or S3
      delay(250);
      lc.setLed(0, 2, 5, false);

      // update display brighness
      adjustBrightness();

      //for debug only
      Serial.print("Range = ");
      Serial.println(bright_lim);
    }


    // check ambient light every 4 seconds
    if (count % 40 == 0)
    {
      adjustBrightness();
    }

    // Flash onboard LED every second
    if (count % 10 == 0)
    {
      digitalWrite(13, !digitalRead(13)); // toggle led https://www.baldengineer.com/arduino-toggling-outputs.html
    }
  }
}


