// sequence through display as for start up
// this has no practical purpose other than to look cute
// and dispay s/w version
// and give you the oppertuniy to jump to demo / alignment modes

void st_display(void) {
  lc.clearDisplay(0);
  // display version number for approx 2 second
  lc.setColumn(0, 6, B10000000);
  lc.setColumn(0, 1, B11110000);
  delay(2000);
  // display fill
  for (int count = 0; count < 8; count++)
  {
    lc.setRow(0, count, 255);
    // Check if button 1 held down go into demo mode
    if (digitalRead(button1) == LOW) {
      int count = 0;  // setup time out counter for jump to alignment mode
      while (digitalRead(button1) == LOW)    // wait for button to be released
      {
        delay(100);
        count ++;
        if (count > 20)
        {
          // display alignment grid
          lc.setColumn(0, 0, B10000001);
          lc.setColumn(0, 1, B00000000);
          lc.setColumn(0, 2, B00000000);
          lc.setColumn(0, 3, B00011000);
          lc.setColumn(0, 4, B00011000);
          lc.setColumn(0, 5, B00000000);
          lc.setColumn(0, 6, B00000011);
          lc.setColumn(0, 7, B10000011);
          delay(2000);
          while (digitalRead(button1) == HIGH)  // stay in align mode until S1 pushed
          {
            delay(100);
          }
          lc.clearDisplay(0);
          while (digitalRead(button1) == LOW)   // wait for s1 to be released to avoid going
                                                // back in to align loop
          {
            delay(100);
          }
        }      
      }
      // go to demo mode - you have to hit reset to clear this mode
      demo();
    }
    delay(400);
  }
}
