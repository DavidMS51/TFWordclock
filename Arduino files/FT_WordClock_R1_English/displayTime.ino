
// 'Calculate' and display the correct word phrase based on the min_x and hour_x variables

// To run in alternative langauge comment out / un comment as required and re-compile
void displayTime(void) {

  // *** English character definitions ***
  // define matrix number data for 5 minute slot wording
  // minutes
  byte five_hr[8] = {B00000010, B00000010, B00000000, B00000010, B00000000, B00000010, B00000000, B00000000};
  byte ten_hr[8] = {B00000000, B00000000, B00000000, B00000000, B00000010, B00000000, B00000010, B00000010};
  byte fifteen[8] = {B00000010, B00000010, B00000010, B00000000, B00000010, B00000010, B00000010, B00000010};
  byte twenty[8] = {B00000000, B00000000, B00000001, B00000001, B00000001, B00000001, B00000001, B00000001};
  byte twenty5[8] = {B00000010, B00000010, B00000001, B00000011, B00000001, B00000011, B00000001, B00000001};
  byte half[8] = {B00000101, B00000101, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000};
  byte past[8] = {B00000000, B00000000, B00000000, B00000100, B00000100, B00000100, B00000100, B00000000};
  byte to[8] = {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000100, B00000100};

  // hours
  byte One[8] = {B00010000, B00010000, B00010000, B00000000, B00000000, B00000000, B00000000, B00000000};
  byte Two[8] = {B00100000, B01100000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000};
  byte Three[8] = {B00000000, B00000000, B00000000, B00010000, B00010000, B00010000, B00010000, B00010000};
  byte Four[8] = {B01000000, B01000000, B01000000, B01000000, B00000000, B00000000, B00000000, B00000000};
  byte Five[8] = {B00000000, B00000000, B00000000, B00000000, B01000000, B01000000, B01000000, B01000000};
  byte Six[8] = {B10000000, B10000000, B10000000, B00000000, B00000000, B00000000, B00000000, B00000000};
  byte Seven[8] = {B00000000, B00000000, B00000000, B10000000, B10000000, B10000000, B10000000, B10000000};
  byte Eight[8] = {B00000000, B00000000, B00000000, B00001000, B00001000, B00001000, B00001000, B00001000};
  byte Nine[8] = {B00001000, B00001000, B00001000, B00001000, B00000000, B00000000, B00000000, B00000000};
  byte Ten[8] = {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00111000};
  byte Eleven[8] = {B00000000, B00000000, B00100000, B00100000, B00100000, B00100000, B00100000, B00100000};
  byte Twelve[8] = {B00100000, B00100000, B00100000, B00100000, B00000000, B00100000, B00100000, B00000000};

  // combined result - this is what we will actually display
  byte sum_disp[8] = {B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000};


  // Update the display

  /*
    The following code effectivly segements minutes into five minute slots
    and then displays the correct term.

    The display information is built up in the sum_disp Array using bit wise
    logic 'OR' operations in 3 parts  'minute', 'past/to' and hours

    The serial print statements are include for debug only
  */

  switch (min_x) {
    case 0:
    case 1:
    case 2:
    case 58:
    case 59:
      // this is a dummy case as nothing needs to be shown on the hour
      Serial.print("-- ");
      break;

    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 53:
    case 54:
    case 55:
    case 56:
    case 57:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = five_hr[i];
      }
      Serial.print("Five ");
      break;

    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
    case 48:
    case 49:
    case 50:
    case 51:
    case 52:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = ten_hr[i];
      }
      Serial.print("Ten ");
      break;

    case 13:
    case 14:
    case 15:
    case 16:
    case 17:
    case 43:
    case 44:
    case 45:
    case 46:
    case 47:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = fifteen[i];
      }
      Serial.print("Fifteen ");
      break;

    case 18:
    case 19:
    case 20:
    case 21:
    case 22:
    case 38:
    case 39:
    case 40:
    case 41:
    case 42:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = twenty[i];
      }
      Serial.print("Twenty ");
      break;

    case 23:
    case 24:
    case 25:
    case 26:
    case 27:
    case 33:
    case 34:
    case 35:
    case 36:
    case 37:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = twenty5[i];
      }
      Serial.print("Twenty Five ");
      break;

    case 28:
    case 29:
    case 30:
    case 31:
    case 32:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = half[i];
      }
      Serial.print("Half ");
      break;
  }

  // Sort out 'to' and 'past'
  int hour_tmp = hour_x;       // setup temp version of hour_x [ so orginal value is retained
  if (min_x < 3)
  {
    // dummy nothing to display
    Serial.print("-- ");
  }
  else if (min_x < 33)
  {
    for (int i = 0; i < 8; i++)
    {
      sum_disp[i] = sum_disp[i] | past[i];

    }
    Serial.print("Past ");
  }
  else if (min_x < 58)
  {
    for (int i = 0; i < 8; i++)
    {
      sum_disp[i] = sum_disp[i] | to[i];
    }
    Serial.print("To ");
    hour_tmp++;    // add 1 hour to the time to force correct hour display
  }
  else
  {
    // Dummy nothing to show
    Serial.print("-- ");
    hour_tmp++;   // add 1 hour to the time to force correct hour display
  }

  // Display correct hour

  switch (hour_tmp) {
    case 1:
    case 13:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | One[i];
      }
      Serial.print("one");
      break;

    case 2:
    case 14:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Two[i];
      }
      Serial.print("Two");
      break;

    case 3:
    case 15:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Three[i];
      }
      Serial.print("Three");
      break;

    case 4:
    case 16:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Four[i];
      }
      Serial.print("Four");
      break;

    case 5:
    case 17:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Five[i];
      }
      Serial.print("Five");
      break;

    case 6:
    case 18:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Six[i];
      }
      Serial.print("Six");
      break;

    case 7:
    case 19:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Seven[i];
      }
      Serial.print("Seven");
      break;

    case 8:
    case 20:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Eight[i];
      }
      Serial.print("Eight");
      break;

    case 9:
    case 21:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Nine[i];
      }
      Serial.print("Nine");
      break;

    case 10:
    case 22:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Ten[i];
      }
      Serial.print("Ten");
      break;

    case 11:
    case 23:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Eleven[i];
      }
      Serial.print("Eleven");
      break;

    case 0:
    case 12:
    case 24:
      for (int i = 0; i < 8; i++)
      {
        sum_disp[i] = sum_disp[i] | Twelve[i];
      }
      Serial.print("Twelve");
      break;
  }
  /*
    Now update the display with the product built in sum_disp,
    but first clear the display
  */
  lc.clearDisplay(0);

  lc.setRow(0, 0, sum_disp[0]);
  lc.setRow(0, 1, sum_disp[1]);
  lc.setRow(0, 2, sum_disp[2]);
  lc.setRow(0, 3, sum_disp[3]);
  lc.setRow(0, 4, sum_disp[4]);
  lc.setRow(0, 5, sum_disp[5]);
  lc.setRow(0, 6, sum_disp[6]);
  lc.setRow(0, 7, sum_disp[7]);
  Serial.println();
}

