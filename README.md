# TFWordclock
Repository for Tempus Fugit WordClock s/w and build instructions

Usage: Wordclockr3.py [-h] [-r count] [-b bklopt]  [{English,French,Dutch,German}]
 
positional arguments:
  {English,French,Dutch,German}
                        Language: English, French, Dutch or German (default:English)
optional arguments:
  -h, --help            show this help message and exit
  -r count, --rotation count
                        Rotation - 0 = upright, 1 = rotated 90 clockwise, 2 = upside down
and 3 = 90 counter-clockwise (default: 0)
  -b bklopt, --blink bklopt
                        blink - 0 = board act led only 1:1, 1 = minute indicaton blinking, 2 = board act led only 1:20,
3 =act led off (default: 0)


Notes:

German version not implementedin r3 version

Wordclockrx.py and timewrdxca.py must be in the same directory

where x is the current revision code

Wordclockr3.py
timewrd4ca.py
