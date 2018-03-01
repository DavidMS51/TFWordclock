# TFWordclock
Repository for Tempus Fugit WordClock s/w and build instructions

```
Usage: Wordclockr5.py [-h] [-r count] [-b bklopt]  [{English,French,Dutch,German}]
 
positional arguments:  
  {English,French,Dutch,German}   
                        Language: English, French, Dutch or German (default:English)  
optional arguments:  
  -h, --help            show this help message and exit  
  -r count, --rotation count  
                        Rotation - 0 = upright, 1 = rotated 90 clockwise, 2 =
                        upside down and 3 = 90 counter-clockwise (default: 0)  
  -b bklopt, --blink bklopt  
                        blink - 0 = board act led only 1:1, 1 = minute
                        indication blinking (ignored for French), 2 = board
                        act led only 1:10, 3 = act led off (default: 0)  
```

Notes:

Rev 5  
Language handling change for rev 5 - see python code

Wordclockrx.py and timewrdxca_xx.py must be in the same directory
where x is the current revision code.  
TFW_data file must be in TFWordclock directory 

Current versions

   Wordclockr5.py  
   timewrd5ca_eng.py  
   timewrd5ca_fr.py  
   timewrd5ca_du.py  
   timewrd5ca_ger.py  
