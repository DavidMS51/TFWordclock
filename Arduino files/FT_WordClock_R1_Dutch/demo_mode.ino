
int demo() {
  // clear display and adjust brightness
  lc.clearDisplay(0);
  adjustBrightness();
  // run through hours / minutes display seperatly to start with
  for (int count = 1; count < 13; count++)
  {
    hour_x = count;
    min_x = 0;
    displayTime();
    delay(1000);
  }

  {
    adjustBrightness();
    lc.clearDisplay(0);
    for (int count = 1; count < 60; count = count + 5)
    {
      hour_x = 99;
      min_x = count;
      displayTime();
      delay(1000);
    }

    lc.clearDisplay(0);
    //scroll continiuosly though complete 12 hour display
    // run through hours display
    while (true)
    {
      adjustBrightness(); // check display brigntness every 12 hour loop
      for (int count = 1; count < 13; count++)
      {
        hour_x = count;
        min_x = 0;
        for (int count1 = 1; count1 < 60; count1 = count1 + 5)
        {
          min_x = count1;
          displayTime();
          delay(2000);
          adjustBrightness();   // check brightness is ok
        } 
       
      }
    }
  }
}



