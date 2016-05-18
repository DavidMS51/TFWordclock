
// change brightness based on the time of day.

void adjustBrightness() {
  // read the analog in value an average with previous reading
  // ignore the last reading if more that count movement
  // but only do it once
  
  uncor = analogRead(analogInPin);
  if ((uncor > raw_bright_old + 2 || uncor < raw_bright_old - 2) && c_flag == false) {
    uncor = raw_bright_old;   // revert to last reading
    /*
    Serial.print("Big change ignore ");   // debug only
    Serial.println(); // debug only
    */
    c_flag = true;
  }
  else
    c_flag = false;

  raw_bright = ((uncor + raw_bright_old) / 2); // get raw LDR value
  raw_bright_old = raw_bright;
  switch (raw_bright) {
    case 0 ... 69:
      bright = 0;
      break;

    case 70 ... 149:
      bright = 1;
      break;

    case 300 ... 349:
      bright = 2;
      break;

    case 350 ... 600:
      bright = 3;
      break;

    case 601 ... 699:
      bright = 4;
      break;

    case 700 ... 799:
      bright = 5;
      break;

    case 800 ... 899:
      bright = 6;
      break;

    case 900 ... 984:
      bright = 7;
      break;

    case 985 ... 994:
      bright = 8;
      break;

    case 995 ... 1003:
      bright = 9;
      break;

    case 1004 ... 1008:
      bright = 10;
      break;

    case 1009 ... 1012:
      bright = 11;
      break;

    case 1013 ... 1016:
      bright = 12;
      break;

    case 1017 ... 1019:
      bright = 13;
      break;

    case 1020 ... 1021:
      bright = 14;
      break;

    case 1022 ... 9999:
      bright = 15;
      break;

  }

  
  /* update Max7219 intensity register, based on ambient light
   * level and range limiting variable 
  */
  if (bright > bright_lim) {
    bright = bright_lim;
  }
  lc.setIntensity(0, bright);
}




