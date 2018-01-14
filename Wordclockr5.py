#!/usr/bin/env python

# 8x8 workclock program  - Multi language version
# Requires timewrd5ca.py to be in same folder - this contains the word data.

# To shutdown hold S3 and S2 buttons for about 6 seconds
# To put into time set mode hold down S1, adjust with S2 & S3, set by holding down S1
# To adjust the brightness use S2 and S3
# To run in demo mode hold S1 down during display intro [ not from boot ]
# To put into alignment mode keep holding S1 during intro
# To abort demo mode hold down S2 and S3 - this only works when you get to the
# full clock cycle 

# David Saul https://meanderingpi.wordpress.com/
#
# Release version 5 - See github [https://github.com/DavidMS51/TFWordclock.git] for usage licence details

# From version 5 
#       class has changed to use the luma.led_matrix libuary
#       this is not compatable with earlier vesions using the max7219 which is 
#       if effectcivly obsolete from Dec 2017
# 
#       each language now has it's own timewrd file in the format timewrd5ca_eng.py 
#       this avoids things getting too ungainly and also makes it eaiser
#       to add support for other display in the future
#       
#       support for various status symbol display has changed    


# This is written to work with the timewrd class file  version 5 and higher

# Because of the change of libuary some version 4 features are slightly different / no longer supported
#
#
# --- display rotation  - this is now controlled by setting the variable 'rotation' in timewrd5
# --- only english support currently - can add French and Dutch if there is interest
# --- blink to indicate time within 5 minute incruments - no plans to re-impliment
# --- the various warning are not impliemented as 'count downs' rather than moving bars
# --- Note  blink options do not work with Pi3 because of the way the status led implimented


# luma.led_matrix libuary - Richard Hull
# https://github.com/rm-hull/luma.led_matrix
#
#


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
    parser.add_argument('-b', '--blink', type=int, choices=range(0, 4), default=0, metavar="bklopt", \
    help='blink - 0 = board act led only 1:1, 1 = minute indicaton blinking, 2 = board act led only 1:10, 3 = act led off  (default: %(default)d)')
    parser.add_argument('language', default='English', nargs='?', choices=['English', 'French', 'Dutch', 'German'], help='Language: English ONLY CURRENTLY (default: %(default)s)')

    # Parse the arguments.  Exits if help is called, or there is a problem
    args = parser.parse_args()

    return args


###  MAIN  ###


args = parse_cmd_line()

# Sort out what Language variant will be called
# Default - ie no addtional variable in command line assume English
if args.language == "English":

	from timewrd5ca_eng  import DMS_wrdck as DMS_wrdck



#---
#for emulator use comment out the above and uncomment the below
#from timewrd5ca_eng_e  import DMS_wrdck as DMS_wrdck
#
#Also comment out all references to args
#---

#These are not currently avaialble

#elif args.language == "French":
#	from timewrd5ca_fr  import DMS_wrdck as DMS_wrdck
#
#elif args.language == "Dutch":
#        from timewrd5ca_du  import DMS_wrdck as DMS_wrdck
#
#elif args.language == "German":
#        from timewrd5ca_ger  import DMS_wrdck as DMS_wrdck


#else:
#	print "Invalid language extension " , mod_ext , " not found"
#	sys.exit() 

# Set up class access
wrdck = DMS_wrdck()

# Display selected run settings
print
print
print "Settings are, "
#print "Language =",args.language
print "Rotation = from V5 set via rotation variable in timewrd"

#
print "Blink option =",

if  args.blink  == 0:
	print "board act led only 1:1"

elif args.blink == 1:
	print "minute indication blinking"
elif args.blink == 2:
	print "board act led only 1:10"
elif args.blink == 3:
        print "act led off"
else:
	print "Blink option error"

print 

# Strip out version number from application name
version = sys.argv[0]
version = version[-4:-3] 		# main s/w issue version
print "Version = ", version

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup ports for auto brightness control 
anpin = 24      # analog pin input
smpin = 23      # charge driving output pin

GPIO.setup(anpin,GPIO.IN)
GPIO.setup(smpin,GPIO.OUT)

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
			# show alignment display
			wrdck.align()		#display alignment screen
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



	# First run through minutes display
	cur_time_min = 0
        cur_time_hr = -1

	while cur_time_min < 60:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_min = cur_time_min +1
		sleep(.3)

	# Then hours
	cur_time_min = 0
	cur_time_hr = 1

	while cur_time_hr < 13:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_hr=cur_time_hr+1
		sleep(1.2)

	# Both, run forever
	cur_time_min = 0
	cur_time_hr = 1



	while True:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_min=cur_time_min+1
		if cur_time_min == 60:
			cur_time_min = 0
			cur_time_hr = cur_time_hr +1
			if cur_time_hr == 24:
				cur_time_hr = 1

		if GPIO.input(S3) == False and GPIO.input(S2) == False:	# Check for abort
			wrdck.clear()
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

#	not currently working	
        wrdck.contrast(result*17)       # update display rightness - 17 to get to 17-255 range
        return(result)

#
# Allows the PiZero to be cleanly shut down
def prog_term(bl_lev):
	
	# Checks both keys are held down for 2 seconds before halting, while
	# counting down from 9
	# 
	print
	print "WARNING PI WILL START SHUTDOWN IF KEY HELD FOR 2 SECONDS"
	print
	t = 0
	col = 10
	while col > 0:
		col = col - 1
		while t < 10:
			t=t+1
			# Check the keys are still being held down
			if GPIO.input(S3) == True or GPIO.input(S2) == True:
				# clear and reset the display
				wrdck.clear()	
				wrdck.ckdisp(cur_time_min,cur_time_hr)
				print "Shutdown aborted"
				return()
			sleep(.03)
		wrdck.ckdisp(0,col)
		t = 0

	print "Halting now"
	writebright(bl_lev)	# Try to update brightness level
	wrdck.clear()
	sleep(1)		# just to give the file update time to completed before shutdown starts
	# Halt Pi
	os.system("sudo poweroff")
	sleep(20)		# to stop anything starting during shutdown
#	sys.exit("Exiting- debug")		# for debug only   -when you dont want to keep shutting down


# Allows time to be locally set and RTC hardware clock to updated with new local time
# Only sets hours and minutes. Date is not modifiable locally
def tset():
	cur_time_hrt =int(datetime.now().strftime('%I'))  # These are local variables, so need redefining
        cur_time_mint=int(datetime.now().strftime('%M'))
	wrdck.ckdisp(cur_time_min,cur_time_hrt,'A')	#add astrix to time display to show in setting mode
	# Wait for the S1 button to be released
	while GPIO.input(S1) == False: 
        	sleep(.1)

	sleep(.2)
	tout = 100

	while True:
		tout = tout -1	# Decrement time out counter
		if tout == 0:	# If tout reaches zero drop back to main prog loop without changing time
			# Clear and reset the display
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
			
			wrdck.ckdisp(0,cur_time_hrt,'A') # Display temp time info

                elif GPIO.input(S2) == False:	# Check for S2 push if yes increment minutes counter
                        tout = 100      	# Reset time out flag
                        while GPIO.input(S2) == False:	# Wait until button is released
                                sleep(.1)
                        cur_time_mint = cur_time_mint + 5	# Increment temp minute flag
                        if cur_time_mint > 59:
                                cur_time_mint = 0

                        wrdck.ckdisp(cur_time_mint,-1,'A')	# Display temp time info

		elif GPIO.input(S1) == False:		# Check for S1 push if yes
							# Start time update procedure to hwclock

        		print
		        print "WARNING SYSTEM TIME WILL BE UPDATED IF KEY HELD FOR 3 SECONDS"
		        print
			#clear display and then show diagnal sequence to warn of update is going to happen
			wrdck.clear()
		        t = 0
		        col = -1
		        while col < 7:
                		col = col + 1
                		while t < 4:
                        		t=t+1
                        		# Check the S1 key is still being held down
                        		if GPIO.input(S1) == True:
                        		        # Clear and reset the display
                                		wrdck.ckdisp(cur_time_min,cur_time_hr)
                                		print "Time update aborted"
                                		return()
                        		sleep(.1)
		       	        	wrdck.pixel(col,col)
                		t = 0

			# Time update code - flash letting 'U' at the same time
			date_str = str(cur_time_hrt)+":"+str(cur_time_mint) # Build date_str
        		print "Updating TIME now to ",
			wrdck.pixel(2,6)
			sleep(.25)
			wrdck.clear()
			sleep(.25)
                        wrdck.pixel(2,6)
                        sleep(.25)
                        wrdck.clear()
                        sleep(.25)

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
wrdck.ckdisp(0,(int(version)),'V')	# dislay current version number by setting hour to version and adding V prefix

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
	wrdck.clear()
	sleep(.25)
	count= count +1
	if count > 600:	# If left in fault state for 5 minutes exit the program 
		sys.exit("Exiting, Buttons incorrectly configured")

# Display startup countdown from 5 with option to jump to demo mode
col = 5
while col > 0:
        wrdck.ckdisp(0,col)
        col = col - 1
        if GPIO.input(S1) == False:     # if S1 held down jump to demo / align mode
	 	wrdck.test()
		demo()
                wrdck.clear()    # Clear display
                col = 0                 # Start clock immediatly on return 
        sleep(.75)


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
print "Syncing app timer loop to clock time"

# Sync on multiple of 10 seconds (for 10 sec loop in main loop)
while int(datetime.now().strftime('%S')) % 10 != 0:
	wrdck.init()			#disp 'init' while synicing
wrdck.clear()

# Get an initial time
cur_time_hr  = int(datetime.now().strftime('%H'))
cur_time_min = int(datetime.now().strftime('%M'))
Max_br = setbright(range)


minb = 0	# tmp varible for minute blinking only

#Main time display loop
while True:
	# Update display
	wrdck.ckdisp(cur_time_min,cur_time_hr)
	print "hr = ",cur_time_hr," mn = ",cur_time_min, " Max7219 brightness setting = ", Max_br, " Range 1 -", range

	# Wait until minute changes before calling display update again
	temp = cur_time_min

	while cur_time_min == temp:
		
		# Autoset display brightness based on ambient light level
	        Max_br = setbright(range)
#		nblinks = cur_time_min % 5	# Number of blinks to indicate minute in 5 minute interval
		t = 0
		# 10 sec delay with button check and minute blinking
		while t < 100:
			if t > 90 and int(datetime.now().strftime('%S')) % 10 == 0:
				t = 99		# Synchronize on 10 sec interval
			t = t + 1
			# Flash PiZero board LED blinks options - note this does not work with a Pi3
			if args.blink == 1:	# if blink = 1 flash once minute for 1/10 sec
				if t % 10 == 0:
					minb = minb +1
					if minb == 60:
						minb = 0
	                                        GPIO.output(47,GPIO.LOW)
        	                                sleep(.1)
                	                        GPIO.output(47,GPIO.HIGH)

			elif args.blink == 2:	# if blink = 2 flash once every 10 sec for 1/10 sec
				if t == 100:
					GPIO.output(47,GPIO.LOW)
					sleep(0.1)
					GPIO.output(47,GPIO.HIGH)
			elif args.blink == 3:			# act led off
					GPIO.output(47,GPIO.HIGH)	# make certain LED is off
			else:
				if t % 10 == 0:
					if fl == True:
						GPIO.output(47,GPIO.HIGH)
						fl = False
					else:	
						GPIO.output(47,GPIO.LOW)
						fl = True

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
					pass
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
						wrdck.ckdisp(cur_time_min,cur_time_hr,'A')	# Set astrix for positive feedback
						sleep(.5)
					Max_br = setbright(range)	# Set new brightness level
					wrdck.ckdisp(cur_time_min,cur_time_hr)	# Clear astrix

				elif GPIO.input(S3) == False:   # Increase range setting
                	                range = range + 1
                        	        if range >= 15:		# Stop out range numbers for range
                                	        range = 15
						wrdck.high(True)	# Set display high limit warning
						sleep(.5)
			                        wrdck.high(False)	# Clear display high limit warning
                	                while GPIO.input(S3) == False:	# Wait for button to be released
						wrdck.ckdisp(cur_time_min,cur_time_hr,'A')	# Set astrix for positive feedback
                        	                sleep(.2)
                                	Max_br = setbright(range)	# Set new brightness level
					wrdck.ckdisp(cur_time_min,cur_time_hr)	# Clear astrix
				print "range ", range
				# Refresh the display
			        wrdck.ckdisp(cur_time_min,cur_time_hr)

			sleep(.1)

		cur_time_min = int(datetime.now().strftime('%M'))

	cur_time_hr = int(datetime.now().strftime('%H'))	# Update local hour time variable
