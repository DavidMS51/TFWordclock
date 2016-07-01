#!/usr/bin/env python

# 8x8 workclock program  - Multi language version
# Requires timewrd4ca.py to be in same folder - this contains the word data.

# To shutdown hold S3 and S2 buttons for about 6 seconds
# To put into time set mode hold down S1, adjust with S2 & S3, set by holding down S1
# To adjust the brightness use S2 and S3
# To run in demo mode hold S1 down during display intro [ not from boot ]
# To put into alignment mode keep holding S1 during intro
# To abort demo mode hold down S2 and S3 - this only works when you get to the
# full clock cycle 

# David Saul https://meanderingpi.wordpress.com/
#
# Release version 3 - See github [https://github.com/DavidMS51/TFWordclock.git]
# for usage licence details
# Simon Reap <simon@simonreap.com> Added text rotation, and argparse for parameter processing.
# Ton van Overbeek <tvoverbeek@gmail.com> Added minute indication by blinking the display (only for English and Dutch)
# Now uses timewrd4ca (with rotation and blinking support) for text.


import os
import sys
import argparse
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

############################################################
# Parse the command-line arguments
############################################################
def parse_cmd_line():
    parser = argparse.ArgumentParser(description='Tempus Fugit Word Clock', epilog='A multi-language word-based clock by David Saul')
# Argparse automatically adds: ('-h', '--help', action='store_true', help='show usage')
    parser.add_argument('-r', '--rotation', type=int, choices=range(0, 4), default=0, metavar="count", help='Rotation - 0 = upright, 1 = rotated 90 clockwise, 2 = upside down and 3 = 90 counter-clockwise (default: %(default)d)')
    parser.add_argument('language', default='English', nargs='?', choices=['English', 'French', 'Dutch'], help='Language: English, French or Dutch (default: %(default)s)')

    # Parse the arguments.  Exits if help is called, or there is a problem
    args = parser.parse_args()

    return args

###  MAIN  ###

args = parse_cmd_line()

# Sort out what Language variant will be called
# Default - ie no addtional variable in command line assume English
if args.language == "English":
	from timewrd4ca  import DMS_wrdck_en as DMS_wrdck

elif args.language == "French":
	from timewrd4ca  import DMS_wrdck_fn as DMS_wrdck

elif args.language == "Dutch":
        from timewrd4ca  import DMS_wrdck_du as DMS_wrdck

else:
	print "Invalid language extension " , mod_ext , " not found"
	sys.exit() 

# Set up class access
wrdck = DMS_wrdck()

# Confirm language setting and rotation count
print '%s - Rotation %d' % (wrdck.lan()	, args.rotation)

# Strip out version number from application name
version = sys.argv[0]
version = version[-4:-3] 		# main s/w issue version
print "Version = ", version

# Define rotation - 0 = upright, 1 = 90 degress clockwise, 2 = upside down, 3 = 90 degs counterclockwise
wrdck.set_rotate(args.rotation)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup ports for auto brightness control 
anpin = 24      # analog pin input
smpin = 23      # charge driving output pin

GPIO.setup(anpin,GPIO.IN)
GPIO.setup(smpin,GPIO.OUT)

# Make prw / activity LED on Pi Zero available for use as GPIO 47
# Redirect tee output to /dev/null to avoid output on screen
os.system("sudo echo none | sudo tee /sys/class/leds/led0/trigger > /dev/null")
GPIO.setup(47,GPIO.OUT)

#------------------------------------------------------------
# Local functions

# Try to read stored brightness level
def readbright():
	try:
		f_dat = open('/home/pi/TFWordclock/TFW_data.txt','r')
		bl_lev = int(f_dat.readline())
		if bl_lev < 2 or bl_lev >15:
			bl_lev = 15 
		f_dat.close()
                print
                print "Bright limit file read ok",

	except: 		# Error reading, default to max level
		print
		print "Bright limit file read error defaulted to",
		bl_lev = 15
		
	print bl_lev
	print
	return bl_lev

# Try to update stored brightness level
def writebright(bl_lev):	
	try:
		if bl_lev < 2 or bl_lev >15:
                        bl_lev = 15
                f_dat = open('/home/pi/TFWordclock/TFW_data.txt','w')
                f_dat.write(str(bl_lev)+'\n')
                f_dat.close()
		print
		print "Stored brightness level updated ok"
		print


        except:                 # error writing new level
                print
                print "Bright limit file write error"
		print

        return 

# Demo mode
def demo():
	count = 0	# Use to time how long S1 is held down
			# If over 2 seconds jump to Align mode first
	while GPIO.input(S1) == False:
		count = count + 1
		sleep (.1)
		if count > 20:	# Jump to align mode
			print
		        print
		        print "Alignment mode"
		        print "Hold down S1 to revert to Demo mode"
		        print
			# Setup alignment display
			wrdck.device.set_byte(0,8,0B10000011)
			wrdck.device.set_byte(0,7,0B00000011)
			wrdck.device.set_byte(0,6,0B00000000)
			wrdck.device.set_byte(0,5,0B00110000)
			wrdck.device.set_byte(0,4,0B00110000)
			wrdck.device.set_byte(0,3,0B00000000)
			wrdck.device.set_byte(0,2,0B00000000)
			wrdck.device.set_byte(0,1,0B10000001)
			while GPIO.input(S1) == False:
                        	sleep(.1)		# wait for S1 to be released
			sleep(1)	
			while GPIO.input(S1) == True:	# wait for S1 to be pushed, then drop back to demo mode
				sleep(.1)

			while GPIO.input(S1) == False:
                                sleep(.1)       # wait for S1 to be released to avoid jumping back
						# into align mode
			sleep(.25)
	print
	print
	print "Starting Demo mode, time increments every second"
	print "Hold down S2 and S3 to terminate"
	print

	wrdck.device.clear(0)

	# First run through minutes display
	cur_time_min = 0
        cur_time_hr = 1

	while cur_time_min < 60:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_min = cur_time_min +1
		sleep(.3)

	# Then hours
	cur_time_min = 0
	cur_time_hr = 0

	while cur_time_hr < 24:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_hr=cur_time_hr+1
		sleep(1.2)

	# Both, run forever
	cur_time_min = 0
	cur_time_hr = 1

	wrdck.device.clear(0)

	while True:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_min=cur_time_min+1
		if cur_time_min == 60:
			cur_time_min = 0
			cur_time_hr = cur_time_hr +1
			if cur_time_hr == 24:
				cur_time_hr = 1

		if GPIO.input(S3) == False and GPIO.input(S2) == False:	# Check for abort
			wrdck.device.clear(0)
			print 
			print "Release keys to start main clock app"
			print
			while GPIO.input(S3) == False or GPIO.input(S2) == False:	# Wait for key release
				sleep(.25)
			return		# Return to main prog start
		sleep(.2)
	
# Sets display brightness based on a combination of ambient light and the range setting
# The range setting acts as a brightness limiter, to accomodate word templates with differing levels
# of 'opaqueness'. The range is set using S2 and S3 in the main program
def setbright(range):

        # setup variable
        count = 0
        delay = 0
        zero = 6 # zero reading
	# Setup corrected range divider - these numbers were derived to 1-15 for a 500 count max
        cor_range = (482,482,238,155,118,94,79,68,59,53,48,43,40,36,34,32)
	
        count = 0

        GPIO.output(smpin,GPIO.HIGH)			# Drive sample pin high to start conversion
        while GPIO.input(anpin) == 0 and count < 500:	# Time how long it takes anpin
                                                        # to go high
                count = count + 1
                sleep(.001)   #0.0005 Bitsbox LDR 0.001 toby LDR

        GPIO.output(smpin,GPIO.LOW)     # Drive sample pin low to discharge capacitor
                                        # Ready for next sample


        # Scale correct result to suit Max brightness setting [ 1-15 / range ]   
        result = int((500-count)/float(cor_range[range]))
        # Ensure result is always valid [ just in case ]
        if result < 1:
                result = 1
        elif result > 15:
                result = 15

        wrdck.device.brightness(result)       # update display rightness
        return(result)

#
# Allows the PiZero to be cleanly shut down
def prog_term(bl_lev):
	# Checks both keys are held down for 2 seconds before halting, while writing
	# 'countdown' bars across the screen
	# 
	print
	print "WARNING PI WILL START SHUTDOWN IF KEY HELD FOR 2 SECONDS"
	print
	t = 0
	col = 0
	while col < 8:
		col = col + 1
		while t < 8:
			t=t+1
			# Check the keys are still being held down
			if GPIO.input(S3) == True or GPIO.input(S2) == True:
				# clear and reset the display
				wrdck.device.clear()	
				wrdck.ckdisp(cur_time_min,cur_time_hr)
				print "Shutdown aborted"
				return()
			sleep(.03)
		wrdck.device.set_byte(0,col,0B11111111)
		wrdck.device.flush()		
		t = 0

	print "Halting now"
	writebright(bl_lev)	# Try to update brightness level
	wrdck.device.clear()
	sleep(1)		# just to give the file update time to completed before shutdown starts
	# Halt Pi
	os.system("sudo poweroff")
	sleep(20)		# to stop anything starting during shutdown

# Allows time to be locally set and RTC hardware clock to updated with new local time
# Only sets hours and minutes. Date is not modifiable locally
def tset():

	# Wait for the S1 button to be released
	while GPIO.input(S1) == False: 
        	sleep(.1)

	sleep(.2)
	tout = 100
	wrdck.device.clear()	# Clear display
	wrdck.astrix(True)	# Show * to indicate device in set mode
	cur_time_hrt =int(datetime.now().strftime('%I'))  # These are local variables, so need redefining
	cur_time_mint=int(datetime.now().strftime('%M'))

	while True:
		tout = tout -1	# Decrement time out counter
		if tout == 0:	# If tout reaches zero drop back to main prog loop without changing time
			# Clear and reset the display
			wrdck.device.clear()
                     	wrdck.ckdisp(cur_time_min,cur_time_hr)
                        print "Time out - time update aborted"
			return

		if GPIO.input(S3) == False:	# Check for S3 push if yes increment hour counter
			tout = 100		# Reset time out flag
			while GPIO.input(S3) == False:	# Wait until button is released
				sleep(.1)
			cur_time_hrt = cur_time_hrt + 1	# Increment temp hour flag 
			if cur_time_hrt == 13:
				cur_time_hrt = 1
			
			wrdck.ckdisp(0,cur_time_hrt) # Display temp time info
			wrdck.astrix(True)

                elif GPIO.input(S2) == False:	# Check for S2 push if yes increment minutes counter
                        tout = 100      	# Reset time out flag
                        while GPIO.input(S2) == False:	# Wait until button is released
                                sleep(.1)
                        cur_time_mint = cur_time_mint + 5	# Increment temp minute flag
                        if cur_time_mint > 59:
                                cur_time_mint = 0

                        wrdck.ckdisp(cur_time_mint,-1)	# Display temp time info
                        wrdck.astrix(True)

		elif GPIO.input(S1) == False:		# Check for S1 push if yes
							# Start time update procedure to hwclock

        		print
		        print "WARNING SYSTEM TIME WILL BE UPDATED IF KEY HELD FOR 3 SECONDS"
		        print

			wrdck.ckdisp(cur_time_mint,cur_time_hrt)	# Display temp time info

		        t = 0
		        col = -1
		        while col < 7:
                		col = col + 1
                		while t < 8:
                        		t=t+1
                        		# Check the S1 key is still being held down
                        		if GPIO.input(S1) == True:
                        		        # Clear and reset the display
                                		wrdck.device.clear()
                                		wrdck.ckdisp(cur_time_min,cur_time_hr)
                                		print "Time update aborted"
                                		return()
                        		sleep(.1)
	       	        	wrdck.device.pixel(col,col,1,1)
                		t = 0

        		wrdck.device.clear()
        		
			# Time update code
			date_str = str(cur_time_hrt)+":"+str(cur_time_mint) # Build date_str
        		print "Updating TIME now to ",
			print date_str  # for test only
			os.system('sudo date -s %s' % date_str)	# Update system time
			sleep(.5)	
			os.system('sudo hwclock -w')	# Update hwclock 
			sleep(.5)
			os.system('sudo hwclock -r')	# Check - for test only

			# Now refresh the display and return to main loop
                        wrdck.ckdisp(int(datetime.now().strftime('%M')),int(datetime.now().strftime('%I')))	
			sleep(2)
			return()
 		sleep(.1)

# End of local functions
#------------------------------------------------------------

# Print startup message to terminal
print
print
print "Starting Matrix Clock Application"
print	
print "S1 for demo mode"
print

# Display Version number
wrdck.ver(int(version))	# dislay current version number

sleep(2)

# Set up buttons to their GPIO numbers (Broadcom numbering)
# This is different from the veroboard prototype
S1 = 27 	# select
S2 = 17		# down	
S3 = 22		# up	

GPIO.setup(S1,GPIO.IN)	
GPIO.setup(S2,GPIO.IN)
GPIO.setup(S3,GPIO.IN)

# Check pushes are not active
# This stops the programme automatically after 5 minutes
# when the pushes are not correctly connected - good for debug
# This is included as it is possible that the s/w will assume you want to 
# shut down the Pi if it in error thinks S2 and S3 are being held down
count = 0
while GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1)== False:
        wrdck.error()
        sleep(.25)
	wrdck.device.clear()
	sleep(.25)
	count= count +1
	if count > 600:	# If left in fault state for 5 minutes exit the program 
		sys.exit("Exiting, Buttons incorrectly configured")

# Display startup graphic with option to jump to demo mode
col = 8
while col > 0:
        wrdck.device.set_byte(0,col,0B11111111)
        col = col - 1
        if GPIO.input(S1) == False:     # if S1 held down jump to demo / align mode
                demo()
                wrdck.device.clear()    # Clear display
                col = 0                 # Start clock immediatly on return 
        sleep(.25)
sleep(1)		# Wait for things to settle down


t = 0			# Initialize temp counter for later
fl= 0			# Setup led flash flag

range = readbright()	# Set range of brightness level to stored value if available
			# If this fails it defaults to 15
			# The software will modify the Max7219 brightness setting based
			# on the ambient light level within this range setting
			# A range setting of 15 will allow 15 brightness settings
			# A range seeting of 1 will lock the brightness at it lowest setting

print
print
print "Starting Clock Application"

# Sync on multiple of 10 seconds (for 10 sec loop in main loop)
while int(datetime.now().strftime('%S')) % 10 != 0:
	pass

# Get an initial time
cur_time_hr  = int(datetime.now().strftime('%H'))
cur_time_min = int(datetime.now().strftime('%M'))
Max_br = setbright(range)

while True:
	# Update display
	wrdck.ckdisp(cur_time_min,cur_time_hr)
	print "hr = ",cur_time_hr," mn = ",cur_time_min, " Max7219 brightness setting = ", Max_br, " Range 1 -", range

	# Wait until minute changes before calling display update again
	temp = cur_time_min
	while cur_time_min == temp:
		
		# Autoset display brightness based on ambient light level
	        Max_br = setbright(range)

		nblinks = cur_time_min % 5	# Number of blinks to indicate minute in 5 minute interval
		blink = t = 0
		# 10 sec delay with button check and minute blinking
		while t < 100:
			if t > 90 and int(datetime.now().strftime('%S')) % 10 == 0:
				t = 99		# Synchronize on 10 sec interval
			t = t + 1

			# Flash PiZero board LED every second
			if t % 10 == 0:
				if fl == True:
					GPIO.output(47,GPIO.HIGH)
					fl = False
				else:	
					GPIO.output(47,GPIO.LOW)
					fl = True

				# Blink display to indicate minute in 5-minute interval except for French
				second = t / 10
				if blink < nblinks and args.language != "French":
					if second & 1:
						# blink off
						wrdck.ckdisp(cur_time_min,cur_time_hr,True)
					else:
						# blink on
						blink = blink + 1
						wrdck.ckdisp(cur_time_min,cur_time_hr)

			# Check for button press
			if GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1) == False:
                                # Check for time set mode
                                if GPIO.input(S1) == False:
                                        tset()
                                        # Refresh working time variables
                                        cur_time_min = int(datetime.now().strftime('%M'))
                                        cur_time_hr  = int(datetime.now().strftime('%H'))

				sleep(.1)	# Delay a bit to make sure all the button presses are captured		
				# Check for shutdown
				if GPIO.input(S3) == False and GPIO.input(S2) == False:
					prog_term(range)	# Passes bightness limit level for storing

				# Check for decrease /  increase display brightness range 	
				elif GPIO.input(S2) == False:	# Decrease range setting
					range = range - 1
					if range <= 1:		# Stop out range numbers for range
						range = 1
						wrdck.low(True)	# Set display low limit warning for bit
						sleep(.5)
						wrdck.low(False)        # Clear any display low limit warning
					while GPIO.input(S2) == False:	# Wait for button to be released
						wrdck.astrix(True)	# Set astrix for positive feedback
						sleep(.5)
					Max_br = setbright(range)	# Set new brightness level
					wrdck.astrix(False)	# Clear astrix

				elif GPIO.input(S3) == False:   # Increase range setting
                	                range = range + 1
                        	        if range >= 15:		# Stop out range numbers for range
                                	        range = 15
						wrdck.high(True)	# Set display high limit warning
						sleep(.5)
			                        wrdck.high(False)	# Clear display high limit warning
                	                while GPIO.input(S3) == False:	# Wait for button to be released
						wrdck.astrix(True)	# Set astrix for positive feedback
                        	                sleep(.2)
                                	Max_br = setbright(range)	# Set new brightness level
					wrdck.astrix(False)	# Clear astrix
				print "range ", range
				# Refresh the display
			        wrdck.ckdisp(cur_time_min,cur_time_hr)

			sleep(.1)

		cur_time_min = int(datetime.now().strftime('%M'))

	cur_time_hr = int(datetime.now().strftime('%H'))	# Update local hour time variable
