// manual time update

// button2   = cycle through minutes
// button3   = cycle through hours

void keypress(void) {
  int count = 0;    // setup temp counter value

  // clear the display and show '*' to indicate in set mode
  lc.clearDisplay(0);
  lc.setRow(0, 7, B00000010);
  while (count < 60)    //setup for 6 second time out
  {
    if (digitalRead(button2) == LOW) {
      while (digitalRead(button2) == LOW) // wait for key to be released
      {
        delay(20);
      }
      min_x = min_x + 5;    // incrument minutes
      if (min_x > 59) {
        min_x = 0;
      }
      count = 0;      // reset timeout counter
      displayTime();  // refresh display
    }
    else if (digitalRead(button3) == LOW) {
      while (digitalRead(button3) == LOW) // wait for key to be released
      {
        delay(20);
      }
      hour_x ++;            // incrument hours
      if (hour_x > 12) {
        hour_x = 1;
      }
      count = 0;      // reset timeout counter
      displayTime();  // refresh display
    }
    delay(100);
    count++;
    // if button 1 pressed start low level RTC update process based on revised values for min_x and hour_x
    if (digitalRead(button1) == LOW) {
    update_RTC();    // run update function
    // wait for key to be released and delay a bit to avoid repeats
    // then return
    while (digitalRead(button1) == LOW)
    {
      delay(20);
    }
    delay(1000);
    return;
    }
  }


}
