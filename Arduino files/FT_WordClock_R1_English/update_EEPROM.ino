/* check to see if EEPROM needs to be updated
    The only current uses for the EEPROM are to store
    1) The number of times the EERPOM has been written to
    2) The brightness limiting varaible bright_lim
    it is important that this routine is only called when a variable has been changed
    as the EERPOM has a  speced write line of 100000 cycles
*/

int update_EEPROM() {
  // define temp varbles
  byte w_count[4];
  Serial.print("Checking stored brightness limit level");  // for debug only
  if (bright_lim == EEPROM.read(brlim_add))
  {
    Serial.println(", no action needed");  // for debug only
    return false;    // no need for action just return
  }
  Serial.println();
  Serial.println("Updating Stored bright limit value");
  // First get the existing number of EEPROM writes
  // number of EEPROM writes is stored as 4 8bit bytes which are then 'rebuilt'
  // to a long integer
  w_count[0] = EEPROM.read(wr_no0);   // update EEPROM write counter byte 0
  w_count[1] = EEPROM.read(wr_no1);   // update EEPROM write counter byte 1
  w_count[2] = EEPROM.read(wr_no2);   // update EEPROM write counter byte 2
  w_count[3] = EEPROM.read(wr_no3);   // update EEPROM write counter byte 3

  /* for debug only
    for (int i = 0; i < 4; ++i) {
     Serial.println((int)w_count[i]);
     }
  */
  // rebuild long integer
  unsigned long EEPROM_w = w_count[0];
  EEPROM_w = EEPROM_w * 256 + w_count[1];  // effectively shift the first byte 8 bit positions
  EEPROM_w = EEPROM_w * 256 + w_count[2];
  EEPROM_w = EEPROM_w * 256 + w_count[3];

  //increment it and re-write
  EEPROM_w++;
  //convert long int back to 4 bytes
  w_count[0] = (byte )((EEPROM_w >> 24) & 0xff);
  w_count[1] = (byte )((EEPROM_w >> 16) & 0xff);
  w_count[2] = (byte )((EEPROM_w >> 8) & 0xff);
  w_count[3] = (byte )(EEPROM_w & 0xff);

  /* for debug only
    for (int i = 0; i < 4; ++i) {
    Serial.println((int)w_count[i]);
    }
  */
  // write updated EEPROM write count and new bright_lim value to EEPROM

  EEPROM.write(wr_no0, w_count[0]);
  EEPROM.write(wr_no1, w_count[1]);
  EEPROM.write(wr_no2, w_count[2]);
  EEPROM.write(wr_no3, w_count[3]);

  EEPROM.write(brlim_add, bright_lim);

  Serial.print("Stored bright limit updated, number of EEPROM write = ");
  Serial.println(EEPROM_w);
  Serial.println();




}



