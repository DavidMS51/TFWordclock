#!/usr/bin/env python

# 8x8 workclock program  - Multi langauge version
# Requires timewrd3ca.py to be in same folder - this has the word data in

# to shutdown hold S3 and S2 pushes for about 6 seconds
# to put into time set mode hold down S1, adjust with S2 & S3, set by holding down S1
# to adjust the brightness use S2 and S3
# to run in demo mode hold S1 down during display intro [ not from boot ]
# to put into alignment mode keep holding S1 during intro
# to abort demo mode hold down S2 and S2 - this only works when you get to the
# full clock cycle 

# David Saul https://meanderingpi.wordpress.com/
#
# Release version 2 - See github [ https://github.com/DavidMS51/TFWordclock.git]
# for usage licence detail
# Simon Reap <simon@simonreap.com> Added text rotation, and argparse for parameter processing.
# Now uses timewrd3ca (with rotation support) for text.



import os
import sys
import argparse
from time import sleep
#from timewrd1_French_ca import DMS_wrdck	# setup for calling common anode drive version
import datetime
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

#Sort out what Language variant will be called
#default - ie no addtional variable in command line assume English
if args.language == "English":
	from timewrd3ca  import DMS_wrdck_en as DMS_wrdck

elif args.language == "French":
	from timewrd3ca  import DMS_wrdck_fn as DMS_wrdck

elif args.language == "Dutch":
        from timewrd3ca  import DMS_wrdck_du as DMS_wrdck


else:
	print "invalid langauge extention " , mod_ext , " not found"
	sys.exit() 

#set up class access
wrdck = DMS_wrdck()

#confirm language setting [ ignore the 'none' ] and rotation count
print '%s - Rotation %d' % (wrdck.lan()	, args.rotation)

#strip out version number from application name
version = sys.argv[0]
version = version[-4:-3] 		# main s/w issue version
print "version = ", version

# Define rotation - 0 = upright, 1 = 90 degress clockwise, 2 = upside down, 3 = 90 degs counterclockwise
wrdck.set_rotate(args.rotation)

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup ports for auto brightness control 
anpin = 24      # sudo analalog pin input
smpin = 23      # charge driving output pin

GPIO.setup(anpin,GPIO.IN)
GPIO.setup(smpin,GPIO.OUT)

# make prw / activity LED available for use as GPIO 16
# for some reason return 'none' to screen
os.system("echo none | sudo tee /sys/class/leds/led0/trigger")
GPIO.setup(47,GPIO.OUT)

#------------------------------------------------------------
# Local Sub-Routines

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

	except: 		# error reading default to max level
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

	count = 0	# use to time how long S1 is held down
			# if over 2 seconds jump to Align mode first
	while GPIO.input(S1) == False:
		count = count + 1
		sleep (.1)
		if count > 20:	#jump to align mode
			print
		        print
		        print "Alignment mode"
		        print "Hold down S1 to revert to Demo mode"
		        print
			# setup alignment  display
			wrdck.device.set_byte(0,8,0B10000011)
			wrdck.device.set_byte(0,7,0B00000011)
			wrdck.device.set_byte(0,6,0B00000000)
			wrdck.device.set_byte(0,5,0B00110000)
			wrdck.device.set_byte(0,4,0B00110000)
			wrdck.device.set_byte(0,3,0B00000000)
			wrdck.device.set_byte(0,2,0B00000000)
			wrdck.device.set_byte(0,1,0B10000001)
			while GPIO.input(S1) == False:
                        	sleep(.1)       # wait for S1 to be released
			sleep(1)	
			while GPIO.input(S1) == True:	# wait for S1 to be pushed, then drop back to demo mode
				sleep(.1)

			while GPIO.input(S1) == False:
                                sleep(.1)       # wait for S1 to be released to avoid jumping back
						# into align mode
			sleep(.25)
	print
	print
	print "Starting Demo mode, time incruement every second"
	print "Hold down S2 and S3 to terminate"
	print

	wrdck.device.clear(0)


	# first run through minutes display
	cur_time_min = 0
        cur_time_hr = 1


	while cur_time_min < 60:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_min = cur_time_min +1
		sleep(.3)

	# then hours
	cur_time_min = 0
	cur_time_hr = 0

	while cur_time_hr < 24:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
		cur_time_hr=cur_time_hr+1
		sleep(1.2)

	# both, run forever
	cur_time_min = 0
	cur_time_hr = 1

	wrdck.device.clear(0)

	while True:
		wrdck.ckdisp(cur_time_min,cur_time_hr)
#		print cur_time_hr,cur_time_min		#debug only
		cur_time_min=cur_time_min+1
		if cur_time_min == 60:
			cur_time_min = 0
			cur_time_hr = cur_time_hr +1
			if cur_time_hr == 24:
				cur_time_hr = 1

		if GPIO.input(S3) == False and GPIO.input(S2) == False:	#check for abort
			wrdck.device.clear(0)
			print 
			print "Release keys to start main clock app"
			print
			while GPIO.input(S3) == False or GPIO.input(S2) == False: # wait for key release
				sleep(.25)
			return		# return to main prog start
		sleep(.2)
	
# sets display brightness based on a combination of ambient light and the range setting
# the range setting acts as a brightness limiter, to accomodate word templates with differing levels
# of 'opaqueness'. the range is set using S2 and S3 in the main program
def setbright(range):

        # setup variable
        count = 0
        delay = 0
        zero = 6 # zero reading
	# setup corrected range divider - these numbers were derived to 1-15 for a 500 count max
        cor_range = (482,482,238,155,118,94,79,68,59,53,48,43,40,36,34,32)
	
        count = 0

        GPIO.output(smpin,GPIO.HIGH)    # drive sample pin high to start conversion
        while GPIO.input(anpin) == 0 and count < 500:   # time how long it takes anpin
                                                        # to go high
                count = count + 1
                sleep(.001)   #0.0005 Bitsbox LDR 0.001 toby LDR

        GPIO.output(smpin,GPIO.LOW)     # Drive sample pin low to discharge capacitor
                                        # ready for next sample


        #scale correct result to suit Max brightness setting [ 1-15 / range ]   
        result = int((500-count)/float(cor_range[range]))
#	print "count ", count
#	print "cor_range ", cor_range[range]
#	print "float result ", (500-count)/float(cor_range[range])
        #ensure result is always valid [ just in case ]
        if result < 1:
                result = 1
        elif result > 15:
                result = 15
#	print "result ", result
#	print

        wrdck.device.brightness(result)       # update display rightness
        return(result)

#
# Allows the PiZero to be cleanly shut down
def prog_term(bl_lev):
	# checks both keys are held down for 6 seconds before halting, while writing
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
			# check the keys are still being held down
			if GPIO.input(S3) == True or GPIO.input(S2) == True:
				# clear and reset the display
				wrdck.device.clear()	
				wrdck.ckdisp(cur_time_min,cur_time_hr)
				print "shut down aborted"
				return()
			sleep(.03)
		wrdck.device.set_byte(0,col,0B11111111)
		wrdck.device.flush()		
		t = 0


	print "halting now"

	writebright(bl_lev)	# try to update brightness level
	wrdck.device.clear()
	sleep(1)		# just to give the file update time to completed before shutdown starts
	# halt pi
	os.system("sudo poweroff")
	sleep(20)		# to stop anything starting during shutdown


#
# Allows time to be locally set and RTC hardware clock to updated with
# new local time
# only worryies abouts and minutes date is not modifiable locally
def tset():

	# wait for S1 key to be released
	while GPIO.input(S1) == False: # wait until push is released
                                sleep(.1)

	sleep(.2)
	tout = 100
	wrdck.device.clear()	# clear display
	wrdck.astrix(True)	# show * to indicate device in set mode
	cur_time_hrt=int(datetime.now().strftime('%I'))  # these are local variable so need re defining
	cur_time_mint=int(datetime.now().strftime('%M'))

	while True:
		tout = tout -1	#dec time out counter
		if tout ==0:	# if tout reaches zero drop back to main prog loop with out changing time
			# clear and reset the display
			wrdck.device.clear()
                     	wrdck.ckdisp(cur_time_min,cur_time_hr)
                        print "time out - time update aborted"
			return

		if GPIO.input(S2) == False:	# check for S2 push if yes inc hour counter
			tout = 100	# reset time out flag
			while GPIO.input(S2) == False:	# wait until push is released
				sleep(.1)
			cur_time_hrt=cur_time_hrt+1	# increment temp hour flag 
			if cur_time_hrt == 13:
				cur_time_hrt = 1
			
			wrdck.ckdisp(0,cur_time_hrt) # display temp time info
			wrdck.astrix(True)

                elif GPIO.input(S3) == False:    # check for S3 push if yes inc hour counter
                        tout = 100      # reset time out flag
                        while GPIO.input(S3) == False: # wait until push is released
                                sleep(.1)
                        cur_time_mint=cur_time_mint+5     # increment temp hour flag
                        if cur_time_mint >59:
                                cur_time_mint = 0

                        wrdck.ckdisp(cur_time_mint,-1) # display temp time info
                        wrdck.astrix(True)

		elif GPIO.input(S1) == False:		# check for S1 push if yes
							# start time update procedure to hwclock

        		print
		        print "WARNING SYSTEM TIME  WILL BE UPDATED IF KEY HELD FOR 3 SECONDS"
		        print

			wrdck.ckdisp(cur_time_mint,cur_time_hrt) # display temp time info

		        t = 0
		        col = -1
		        while col < 7:
                		col = col + 1
                		while t < 8:
                        		t=t+1
                        		# check the S1 key is still being held down
                        		if GPIO.input(S1) == True:
                        		        # clear and reset the display
                                		wrdck.device.clear()
                                		wrdck.ckdisp(cur_time_min,cur_time_hr)
                                		print "time update aborted"
                                		return()
                        		sleep(.1)
	       	        	wrdck.device.pixel(col,col,1,1)
                		t = 0


        		print "updating TIME now to ",
        		wrdck.device.clear()
        		
			# time update code
			date_str = str(cur_time_hrt)+":"+str(cur_time_mint) # build date_str
			print date_str  # for test only
			os.system('sudo date -s %s' % date_str)	# update system time
			sleep(.5)	
			os.system('sudo hwclock -w')	# update hwclock 
			sleep(.5)
			os.system('sudo hwclock -r')	# check - for test only

			# now refresh the display and return to main loop
			wrdck.device.clear()		
                        wrdck.ckdisp(int(datetime.now().strftime('%M')),int(datetime.now().strftime('%I')))	
			sleep(2)
			return()
 		sleep(.1)

# print startup message to terminal
print
print
print "Starting Matrix Clock Application"
print	
print "S1 for demo mode"
print

# Display Version number
wrdck.ver(int(version))	# dislay current version number

sleep(2)

#set up buttons to thier GPIO no

# this is different from the veroboard prototype
S1 = 27 	#yellow		- select
S2 = 22		#blue		- up	
S3 = 17		#red		- down	

GPIO.setup(S1,GPIO.IN)	
GPIO.setup(S2,GPIO.IN)
GPIO.setup(S3,GPIO.IN)

# check pushes are not active
# This stops the programme automatically after 5 minute
# if the pushes are not correctly connected - good for debug
# this is included as it is possible that the s/w will assume you want to 
# shut down the pi if it in error thinks s2 and s3 are being helpd down
count = 0
while GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1)== False:
        wrdck.error()
        sleep(.25)
	wrdck.device.clear()
	sleep(.25)
	count= count +1
	if count > 600:		# if left in fault state for 5 minute exit the program 
	        sys.exit("Exiting Momentary pushes incorrectly configured")



#if GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1)== False:
#	wrdck.error()
#	sys.exit("Exiting Momentary pushes incorrectly configured")


# display start_up graphic- with option to jump to demo mode
col = 8
while col > 0:
        wrdck.device.set_byte(0,col,0B11111111)
        col = col - 1
        if GPIO.input(S1) == False:     # if S1 held down jump to demo / align mode
                demo()
                wrdck.device.clear()    # Clear display
                col = 0                 # Start clock immediatly on return 
        sleep(.25)
sleep(1)		# wait for things to settle down

	

t = 0			#initise temp counter for later
fl= 0			#setup led flash flag

range = readbright()	#set range of brightness level to stored value if available
			#if this fails it defaults to 15
			#the software will modify the Max7219 brightness setting based
			#on the ambiant light level within this range setting
			# a range setting of 1 will allow 15   brightness settings
			# a range seeting of 15 will lock the brightness at it lowest setting

#get an initial time
cur_time_hr=int(datetime.now().strftime('%H'))
cur_time_min=int(datetime.now().strftime('%M'))

#ckdisp() take 2 arguments in the min (0-59) and hour (0-12 displays) them
# on an 8x8 matrix suitably coded

print
print
print "Starting Clock Application"


while True:
#	wrdck.device.clear(0)
	# update display
	wrdck.ckdisp(cur_time_min,cur_time_hr)

	# autoset display brightness based on ambient light level
	# Max_br = setbright()
	
	# wait until minute changes before calling display update again
	temp = cur_time_min
#	print cur_time_hr,cur_time_min
	while cur_time_min == temp:
		
		# autoset display brightness based on ambient light level
	        Max_br = setbright(range)


		cur_time_min=int(datetime.now().strftime('%M'))
		print "hr = ",cur_time_hr," mn = ",cur_time_min, " Max7219 brightness setting = ", Max_br, " Range 1 -", range

		t = 0
		while t < 100:			# delay with key push check
			t = t + 1
			# Flash PiZero board LED every second
			if t % 10 == 0:
				if fl == True:
					GPIO.output(47,GPIO.HIGH)
					fl = False
				else:	
					GPIO.output(47,GPIO.LOW)
					fl = True
			sleep(.1)
			if GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1) == False:	# check for button press
                                # check for time set mode
                                if GPIO.input(S1) == False:
                                        tset()
                                        # refresh working time variables
                                        cur_time_min=int(datetime.now().strftime('%M'))
                                        cur_time_hr=int(datetime.now().strftime('%H'))

				sleep(.1)	# delay a bit to make sure all the keys pressed are captured		
				# check for shutdown
				if GPIO.input(S3) == False and GPIO.input(S2) == False:
					prog_term(range)	#passes bightness limit level for storing

				# check for decrease /  increase display brightness range 	
				elif GPIO.input(S3) == False:	#decrease range setting
					range = range - 1
					if range <= 1:		#stop out range numbers for range
						range = 1
						wrdck.low(True)	#set display low limit warning for bit
						sleep(.5)
						wrdck.low(False)        # clear any display low limit warning
					while GPIO.input(S3) == False:	#wait for ket to be released
						wrdck.astrix(True)  # set astrix for positive feedback
						sleep(.5)
					Max_br = setbright(range)	# set new brightness level
					wrdck.astrix(False)  # clear astrix

				elif GPIO.input(S2) == False:   #increase range setting
                	                range = range + 1
                        	        if range >= 15:		#stop out range numbers for range - this is works out to range of 1-2
                                	        range = 15
						wrdck.high(True) #set display high limit warning
						sleep(.5)
			                        wrdck.high(False)         # clear any display high limit warning
                	                while GPIO.input(S2) == False:  #wait for ket to be released
						wrdck.astrix(True)  # set astrix for positive feedback
                        	                sleep(.2)
                                	Max_br = setbright(range)    # set new brightness level
					wrdck.astrix(False)  # clear astrix
				print "range ", range
				# refresh the display
			        wrdck.ckdisp(cur_time_min,cur_time_hr)



	cur_time_hr=int(datetime.now().strftime('%H'))	# update hour working time varaible




