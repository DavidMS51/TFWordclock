#!/usr/bin/env python

# Python Class for use on word clock project
# Assumes and 8x8 matrix common anode type
# David Saul 2018
# This is configured for the PCB layout REV 4 onwards

# From version 5
# 	class has changed to use the luma.led_matrix libuary
# 	this is not compatable with earlier vesions using the max7219 which is
#	if effectcivly obsolete from Dec 2017
#
#	each language has it's own timewrd file in the format timewrd5ca_eng.py
#	this avoids this file getting too ungainly and also makes it eaiser
#	to add support for other display in the future
#
#	support for various status symbol display has changed
#
#
# +++++++++++++++
# +             +
# +    DUTCH    +
# +             +
# +++++++++++++++
#
# This class is written to work with the TFWordclock App version 5 and higher

# Because of the change of libuary some version 4 features are slightly different / no longer supported
#
#
# --- display rotation  - this is now controlled by setting the variable 'rotation' below
# --- blink to indicate time within 5 minute incruments - no plans to re-impliment
# --- the various warning are not impliemented as 'count downs' rather than moving bars


# luma.led_matrix libuary - Richard Hull
# https://github.com/rm-hull/luma.led_matrix
#

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

#-----------------------------------------------------
rotation = 0		#set global rotate (0,1,2,3)
#-----------------------------------------------------


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, rotate = rotation)


import math
from PIL import Image


# Dutch Class
class DMS_wrdck:


	def ckdisp(self,mint,hour, prefix=False, rot=0):


		# Perfor basic error check on variables
	        if mint < 0 or mint > 59:
        		return
	        if hour < -1 or hour > 24:
        	        return

#	        # Correct from 24 hour to 12
 #       	if hour == 0:
                	hour =12
#
#		if hour > 12:
#			hour = hour - 12

	        # Clear the display first by generating new image

		image = Image.new('1', (8, 8))

		# Display additional charater if needed
		if prefix == 'A':		#Display 'V' [Verandering] - for time setting mode
			image.putpixel((7,5), 1)
		elif prefix == 'V':		#Display V - to indicate version number
			image.putpixel((0, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
		else:
			pass

		# Convert minutes into 5 minute slots, with true rounding
        	min = int(round(mint / 5.0))
#                print mint, int(round(mint /5.0))	#debug only

		# Increment 'hour' for > 30 mins past the hour
		if min > 6 and hour != -1:	#except for special case when hour is inhibited
			hour = hour +1
			if hour == 24:
				hour = 12

                # Correct from 24 hour to 12
                if hour == 0:
                        hour =12

                if hour > 12:
                        hour = hour - 12

		#correct for final 2/3 minutes in the hour
                if min == 12:
                        min = 0

		# Bodge to blank hours display during minute setup
		# if hour = -1 force it to 0 so it does not display
#		if hour == -1:
#			hour = 0

#		print "min lookup ",min		# for debug only

		# Display minutes past / to the hour in to nearest 5 minute 'slot'
		if min == 0:	#oclock
			pass
		elif min ==1:	#five_past
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)

		elif min ==2:	#ten_past
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)


		elif min ==3:	#fifteen_past
			image.putpixel((0, 0), 1)
			image.putpixel((1, 0), 1)
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)

		elif min ==4:	#twenty_past
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((2, 2), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min ==5:	#twenty5_past
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((2, 2), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min ==6:	#half_past
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min ==7:	#twenty5_to
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min ==8:	#twenty_to
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min ==9:	#fifteen_to
			image.putpixel((0, 0), 1)
			image.putpixel((1, 0), 1)
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((2, 2), 1)
			image.putpixel((3, 2), 1)

		elif min ==10:	#ten_to

			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((2, 2), 1)
			image.putpixel((3, 2), 1)

		else:	#five_to
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((2, 2), 1)
			image.putpixel((3, 2), 1)

#	        print "sub ",hour,":", min              #For debug only

		# Display the hours
		if hour == -1: # blank hour display
			pass

		elif hour == 1:	#one
	                image.putpixel((5, 4), 1)
        	        image.putpixel((6, 4), 1)
	                image.putpixel((7, 4), 1)

		elif hour ==2:	#two
			image.putpixel((3, 4), 1)
                	image.putpixel((4, 4), 1)
	                image.putpixel((5, 4), 1)
	                image.putpixel((6, 4), 1)

		elif hour ==3:	#three
        	        image.putpixel((4, 6), 1)
	                image.putpixel((5, 6), 1)
        	        image.putpixel((6, 6), 1)
	                image.putpixel((7, 6), 1)

		elif hour ==4:	#four
                	image.putpixel((1, 5), 1)
	                image.putpixel((2, 5), 1)
        	        image.putpixel((5, 5), 1)
	                image.putpixel((6, 5), 1)

		elif hour ==5:	#five
        	        image.putpixel((1, 5), 1)
                	image.putpixel((2, 5), 1)
	                image.putpixel((3, 5), 1)
        	        image.putpixel((4, 5), 1)

		elif hour ==6:	#six
                	image.putpixel((0, 3), 1)
	                image.putpixel((1, 3), 1)
        	        image.putpixel((2, 3), 1)

		elif hour ==7:	#seven
	                image.putpixel((3, 3), 1)
        	        image.putpixel((4, 3), 1)
                	image.putpixel((5, 3), 1)
	                image.putpixel((6, 3), 1)
        	        image.putpixel((7, 3), 1)

		elif hour ==8:	#eight
			image.putpixel((0, 6), 1)
			image.putpixel((1, 6), 1)
			image.putpixel((2, 6), 1)
			image.putpixel((3, 6), 1)

		elif hour ==9:	#nine
	                image.putpixel((0, 4), 1)
        	        image.putpixel((1, 4), 1)
                	image.putpixel((2, 4), 1)
	                image.putpixel((6, 4), 1)
	                image.putpixel((7, 4), 1)

		elif hour ==10:	#ten
       	        	image.putpixel((0, 5), 1)
	                image.putpixel((2, 5), 1)
        	        image.putpixel((5, 5), 1)
        	        image.putpixel((7, 5), 1)

		elif hour ==11:	#eleven
                	image.putpixel((0, 7), 1)
	                image.putpixel((1, 7), 1)
        	        image.putpixel((7, 7), 1)

		else:	#twelve
        	        image.putpixel((2, 7), 1)
	                image.putpixel((3, 7), 1)
        	        image.putpixel((4, 7), 1)
                	image.putpixel((5, 7), 1)
	                image.putpixel((6, 7), 1)
        	        image.putpixel((7, 7), 1)

		# update the output drivers
        	device.display(image)

        # admin displays ENGLISH
        # these allow the variuos setup and status displays to be
        # language specific without need to change the main code        

        def init(self):
		image = Image.new('1', (8, 8))
		image.putpixel((5, 0), 1)
		image.putpixel((7, 0), 1)

                # update the output drivers
                device.display(image)

        def error(self):
		image = Image.new('1', (8, 8))
		image.putpixel((3, 1), 1)
		image.putpixel((4, 1), 1)

                # update the output drivers
                device.display(image)

        def high(self,state):   # display or clear 'H'
		image = Image.new('1', (8, 8))

                if state == True:
                        image.putpixel((4, 2), 1)

                else:
                        image.putpixel((4, 2), 0)


                # update the output drivers
                device.display(image)


        def low(self,state):    # display or clear 'L'
		image = Image.new('1', (8, 8))

                if state == True:       
			image.putpixel((6, 2), 1)
                else:
			image.putpixel((6, 2), 0)


                # update the output drivers
                device.display(image)

	def test(self):		#display the work test to indicate you are entering demo mode
                image = Image.new('1', (8, 8))
		image.putpixel((0, 5), 1)
		image.putpixel((1, 4), 1)
		image.putpixel((2, 3), 1)
		image.putpixel((3, 4), 1)

                # update the output drivers
                device.display(image)

	def align(self):	#display alignment screen
		image = Image.new('1', (8, 8))
                image.putpixel((0, 0), 1)
                image.putpixel((6, 0), 1)
                image.putpixel((7, 0), 1)
                image.putpixel((6, 1), 1)
                image.putpixel((7, 1), 1)
                image.putpixel((2, 3), 1)
                image.putpixel((3, 3), 1)
                image.putpixel((2, 4), 1)
                image.putpixel((3, 4), 1)
                image.putpixel((0, 7), 1)
                image.putpixel((7, 7), 1)

                # update the output drivers
                device.display(image)

	def pixel(self,x,y):		#allows external app to set an individual pixel
		image = Image.new('1', (8, 8))
                image.putpixel((x, y), 1)

		# update the output drivers
                device.display(image)

	def clear(self):	# clear the current display
		image = Image.new('1', (8, 8))
		# update the output drivers
                device.display(image)

	def contrast(self,level):	# set the birghtness level
		if level > 255 or level < 0:
			return
		device.contrast(level)
