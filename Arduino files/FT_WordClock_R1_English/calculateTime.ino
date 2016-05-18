
// This needs to be re-written to work for UK as a base case

/*
 *  Function to figure out if we're in Daylight Saving Time, then adding an hour if we are in DST.
 *  Inspired by the work of Andy Doro - NeoPixel WordClock from the Adafruit website who adapted used work from nseidle
 *  https://github.com/nseidle/Daylight_Savings_Time_Example/blob/master/Daylight_Savings_Time_Example.ino
 *
 *  This algorithm has two options to observe Daylight Saving Time 
 *  
 *      United States, where as of the time of writing  DST is observed
 *      between the second Sunday in March and the first Sunday in November.
 *      
 *      UK / Europe where as of the time of writing  DST is observed
 *      between the last Sunday in March and the first Sunday in October.
 *      
 *You can check if these work for your location - https://en.wikipedia.org/wiki/Daylight_saving_time_by_country
 *
 *  If you're in a location which observes DST differently this code will need to be modified. If you're lucky enough to not observe DST
 *  then much of this code can be commented out!
 *
 *  This method doesn't check whether its 2am or not when the time change officially occurs. This could be more accurate at the expense of being more complicated.
 *
 */
/*
DateTime calculateTime() {

  DateTime RTCTime = RTC.now();

  if (OBSERVE_DST == 1) {
    if (checkDst() == true) {
      RTCTime = RTCTime.unixtime() + 3600;  // add 1 hour or 3600 seconds to the time
    }
  }

  Serial.print(RTCTime.year(), DEC);
  Serial.print('/');
  Serial.print(RTCTime.month(), DEC);
  Serial.print('/');
  Serial.print(RTCTime.day(), DEC);
  Serial.print(' ');
  Serial.print(RTCTime.hour(), DEC);
  Serial.print(':');
  Serial.print(RTCTime.minute(), DEC);
  Serial.print(':');
  Serial.print(RTCTime.second(), DEC);
  Serial.println();

  return RTCTime;
}

boolean checkDst() {

  DateTime RTCTime = RTC.now();

  //Get the day of the week. 0 = Sunday, 6 = Saturday
  int previousSunday = RTCTime.day() - RTCTime.dayOfTheWeek();

  boolean dst = false; //Assume we're not in DST
  if (RTCTime.month() > 3 && RTCTime.month() < 11) dst = true; //DST is happening!

  //In March, we are DST if our previous Sunday was on or after the 8th.
  if (RTCTime.month() == 3)
  {
    if (previousSunday >= 8) dst = true;
  }
  //In November we must be before the first Sunday to be dst.
  //That means the previous Sunday must be before the 1st.
  if (RTCTime.month() == 11)
  {
    if (previousSunday <= 0) dst = true;
  }

  return dst;

}
*/
