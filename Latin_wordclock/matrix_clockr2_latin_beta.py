#!/usr/bin/env python

# Basic 8x8 workclock program  - LATIN version
# Requires timewrd1_latin_ca.py to be in same folder - this has the word data in

# to shutdown hold red and blue pushs for about 6 seconds

# Demo / basic version only, this does not have a number of the features in the main
# TF WordClock application

import os
import sys
from time import sleep
from timewrd1_Latin_ca import DMS_wrdck	# setup for calling common anode drive version
import datetime
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# make prw / activity LED available for use as GPIO 16
os.system("echo none | sudo tee /sys/class/leds/led0/trigger")
GPIO.setup(47,GPIO.OUT)

#set up class access
wrdck = DMS_wrdck()

def prog_term():
	# checks both keys are held down for 6 seconds before halting, while writing
	# 'countdown' bars across the screen
	# 
	print
	print "WARNING PI WILL START SHUTDOWN IF KEY HELD FOR 3 SECONDS"
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
				wrdck.ckdisp(cur_time_hr)
				print "shut down aborted"
				return()
			sleep(.1)
		wrdck.device.set_byte(0,col,0B11111111)
		wrdck.device.flush()		
		t = 0


	print "halting now"
	wrdck.device.clear()
	sleep(2)
	# halt pi
	os.system("sudo poweroff")
	sleep(20)

def tset():

	# wait for S1 key to be released
	while GPIO.input(S1) == False: # wait until push is released
                                sleep(.1)

	sleep(.2)
	tout = 100
	wrdck.device.clear()	# clear display
	wrdck.device.pixel(2,2,1,1)	# shoe * to indicate device in set mode
	cur_time_hrt=int(datetime.now().strftime('%I'))  # these are local variable so need re defining

	while True:
		tout = tout -1	#dec time out counter
		if tout ==0:	# if tout reaches zero drop back to main prog loop with out changing time
			# clear and reset the display
			wrdck.device.clear()
                     	wrdck.ckdisp(cur_time_hr)
                        print "time out - time update aborted"
			return

		if GPIO.input(S3) == False:	# check for S3 push if yes inc hour counter
			tout = 100	# reset time out flag
			while GPIO.input(S3) == False:	# wait until push is released
				sleep(.1)
			cur_time_hrt=cur_time_hrt+1	# increment temp hour flag 
			if cur_time_hrt == 25:
				cur_time_hrt = 1

			wrdck.ckdisp(cur_time_hrt) # display temp time info
			wrdck.device.pixel(2,2,1,1)
			print cur_time_hrt	# for debug only


		elif GPIO.input(S1) == False:		# check for S1 push if yes
							# start time update procedure to hwclock

        		print
		        print "WARNING SYSTEM TIME  WILL BE UPDATED IF KEY HELD FOR 3 SECONDS"
		        print
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
                                		wrdck.ckdisp(cur_time_hr)
                                		print "time update aborted"
                                		return()
                        		sleep(.1)
	       	        	wrdck.device.pixel(col,col,1,1)
                		t = 0


        		print "updating TIME now"
        		wrdck.device.clear()

        		# time update code
			date_str = str(cur_time_hrt)+":00" # build date_str
			print date_str  # for test only
			os.system('sudo date -s %s' % date_str)	# update system time
			sleep(.5)	
			os.system('sudo hwclock -w')	# update hwclock 
			sleep(.5)
			os.system('sudo hwclock -r')	# check - for test only

			wrdck.device.clear()			# re-fresh the display
                        wrdck.ckdisp(cur_time_hr)
			sleep(2)
			return()
 		sleep(.1)


#set up buttons to thier GPIO no

# this is different from the veroboard prototype
S1 = 27 	#yellow		- select
S2 = 22		#blue		- up	
S3 = 17		#red		- down	

GPIO.setup(S1,GPIO.IN)	
GPIO.setup(S2,GPIO.IN)
GPIO.setup(S3,GPIO.IN)

# check pushes are not active
# This stops the programme automatically shuting down the Pi
# if the pushes are not correctly connected - good for debug

if GPIO.input(S3) == False or GPIO.input(S2) == False or GPIO.input(S1)== False:
	wrdck.device.pixel(3,2,1,1)
	wrdck.device.pixel(2,4,1,1)
	wrdck.device.pixel(5,4,1,1)
	sys.exit("Momentary pushes incorrectly configured  - terminating Clock")
	




t = 0		#initise temp counter for later
fl= 0		#setup led flash flag

#get an initial time
cur_time_hr=int(datetime.now().strftime('%-H'))
cur_time_min=int(datetime.now().strftime('%M'))

#ckdisp() take 1 argument  hours (0-24 displays) them
# on an 8x8 matrix suitably coded

print
print
print "Starting Latin Version of  Clock Application"
print "Demo / basic version only, this does not have a number of the features"
print "of the main TF application"

wrdck.device.brightness(15)	# set display to max bightness

while True:
#	wrdck.device.clear(0)
	# update display
	wrdck.ckdisp(cur_time_hr)
	
	# wait until minute changes before calling display update again
	temp = cur_time_min
#	print cur_time_hr,cur_time_min
	while cur_time_min == temp:
		cur_time_min=int(datetime.now().strftime('%M'))
		print "hr",cur_time_hr,"mn",cur_time_min
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
			if GPIO.input(S3) == False and GPIO.input(S2) == False:
				prog_term()
			elif GPIO.input(S1) == False:
				tset()		

	cur_time_hr=int(datetime.now().strftime('%-H'))	




