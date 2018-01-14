# TFWordclock
Repository for Tempus Fugit WordClock s/w and build instructions

Usage: Wordclockr3.py [-h] [-r count] [-b bklopt]  [{English,French,Dutch,German}]
 
positional arguments:
  {English,French,Dutch,German}
                        Language: English, French, Dutch or German (default:English)
optional arguments:
  -h, --help            show this help message and exit
  -b bklopt, --blink bklopt
                        blink - 0 = board act led only 1:1, 1 = minute indicaton blinking, 2 = board act led only 1:20,
3 =act led off (default: 0)


Notes:

Frech, Dutch and German versions not currently implemented in r5 version

Rev 5
Language handling change for rev 5 - see python code
Rotation now implimented in hardcode - see 
Blink option 1 now works !

Wordclockrx.py and timewrdxca.py must be in the same directory
TFW_data file must be in TFWordclock directory 

where x is the current revision code timewrd5ca_en.py / instructions for details

Wordclockr5.py
timewrd5ca_en.py

[there never was and Wordclockr4]
