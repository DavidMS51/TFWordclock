
// check for button 1, if active start TRC update proccess
int update_RTC(){
    if (digitalRead(button1) == LOW) {
      Serial.println();
      Serial.println("RTC update process STARTED");
      lc.clearDisplay(0);   // clear display

      // display diagnol line
      for (int count = 0; count < 8; count++)
      {
        lc.setRow(0, count, 1 << count);
        delay(500);
        if (digitalRead(button1) == HIGH) {
          Serial.println("RTC update ABORTED");
          Serial.println();
          return false;
        }

      }
      // This line sets the RTC with an explicit date & time, for example to set
      RTC.adjust(DateTime(2016, 6, 1, hour_x, min_x, 0));
      Serial.println("RTC update UPDATED");
      lc.clearDisplay(0);   // clear display
      return true;
    }
}
