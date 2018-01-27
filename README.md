# TFWordclock
Repository for Tempus Fugit WordClock s/w and build instructions

Usage: Wordclockr5.py [-h] [-b bklopt]  [{English,French,Dutch,German}]
 
positional arguments:
  {English,French,Dutch,German}   [German not current available]
                        Language: English, French, Dutch or German (default:English)
optional arguments:
  -h, --help            show this help message and exit
  -b bklopt, --blink bklopt
                        blink - 0 = board act led only 1:1, 1 = minute flash, 2 = 10sec flash,
3 =act led off (default: 0)


Notes:

German version not currently implemented

Rev 5
Language handling change for rev 5 - see python code
Rotation now implimented in hardcode - see instructions

Wordclockrx.py and timewrdxca.py must be in the same directory
TFW_data file must be in TFWordclock directory 

where x is the current revision code
Current versions

   Wordclockr5.py
   timewrd5ca_en.py

[there never was and Wordclockr4]
