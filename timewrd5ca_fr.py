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
# ++++++++++++++++
# +              +
# +    FRENCH    +
# +              +
# ++++++++++++++++
#
# This class is written to work with the TFWordclock App version 5 and higher

# Because of the change of libuary some version 4 features are slightly different / no longer supported
#
#
# --- display rotation  - this is now controlled by setting the variable 'rotation' below
# --- only english and French support currently - can add Dutch if there is interest
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


# French Class
class DMS_wrdck:


	def ckdisp(self,min,hour, prefix=False):


		# Perfor basic error check on variables
	        if min < 0 or min > 59:
        		return
	        if hour < -1 or hour > 24:
        	        return

	        # Clear the display first by generating new image

		image = Image.new('1', (8, 8))

		# Display additional charater if needed
		if prefix == 'A':		#Display astrix - for time setting mode
			image.putpixel((2, 6), 1)
		elif prefix == 'V':		#Display EN and number - to indicate version number
			image.putpixel((4, 7), 1)
			image.putpixel((5, 7), 1)
		else:
			pass

                # Correct from 24 hour to 12
                if hour == 0:
                        hour =1

		# Display minutes past / to the hour in to nearest 15 minute 'slot'

#	        print "sub ",hour,":", min              #For debug only


		# Sort out special cases for midnight and midday, but surpress for count downs etc
                if min < 8 and prefix == False and hour == 12:
			image.putpixel((0, 5), 1)
			image.putpixel((2, 5), 1)
			image.putpixel((5, 5), 1)
			image.putpixel((6, 5), 1)


                elif min < 8 and prefix == False and  hour == 0:
			image.putpixel((2, 7), 1)
			image.putpixel((3, 7), 1)
			image.putpixel((5, 7), 1)
			image.putpixel((6, 7), 1)
			image.putpixel((7, 7), 1)
			image.putpixel((7, 6), 1)


                elif min > 52 and hour == 11:
			image.putpixel((0, 5), 1)
			image.putpixel((2, 5), 1)
			image.putpixel((5, 5), 1)
			image.putpixel((6, 5), 1)

                elif min > 52 and hour == 23:
			image.putpixel((2, 7), 1)
			image.putpixel((3, 7), 1)
			image.putpixel((5, 7), 1)
			image.putpixel((6, 7), 1)
			image.putpixel((7, 7), 1)
			image.putpixel((7, 6), 1)


                # Everything else - hours
                else:   
			
                        # Increment 'hour' for > 30 mins past the hour and you are not in demo
                        if min > 37 and hour !=-1:
                                hour = hour +1
                                if hour == 24:
                                        hour = 1        


			# Display the hours
			if hour == -1: # blank hour display
				pass

			elif hour == 1 or hour == 13:	#one
		                image.putpixel((1, 2), 1)
	        	        image.putpixel((2, 3), 1)
		                image.putpixel((3, 3), 1)

			elif hour ==2 or hour == 14:	#two
				image.putpixel((0, 0), 1)
                		image.putpixel((2, 0), 1)
	                	image.putpixel((3, 0), 1)
	                	image.putpixel((6, 0), 1)

			elif hour ==3 or hour == 15:	#three
        		        image.putpixel((0, 1), 1)
	        	        image.putpixel((1, 1), 1)
        	        	image.putpixel((2, 1), 1)
        		        image.putpixel((4, 1), 1)
        		        image.putpixel((5, 1), 1)

			elif hour ==4 or hour == 16:	#four
                		image.putpixel((0, 2), 1)
		                image.putpixel((1, 2), 1)
        		        image.putpixel((2, 2), 1)
		                image.putpixel((3, 2), 1)
		                image.putpixel((4, 2), 1)
		                image.putpixel((5, 2), 1)

			elif hour ==5 or hour == 17:	#five
	        	        image.putpixel((0, 3), 1)
        	        	image.putpixel((0, 4), 1)
	        	        image.putpixel((1, 4), 1)
        	        	image.putpixel((2, 4), 1)

			elif hour ==6 or hour == 18:	#six
        	        	image.putpixel((4, 0), 1)
	        	        image.putpixel((5, 0), 1)
        	        	image.putpixel((6, 0), 1)

			elif hour ==7 or hour == 19:	#seven
		                image.putpixel((5, 1), 1)
        		        image.putpixel((5, 2), 1)
                		image.putpixel((6, 2), 1)
		                image.putpixel((7, 2), 1)

			elif hour ==8 or hour == 20:	#eight
				image.putpixel((1, 3), 1)
				image.putpixel((4, 3), 1)
				image.putpixel((5, 3), 1)
				image.putpixel((6, 3), 1)

			elif hour ==9 or hour == 21:	#nine
		                image.putpixel((2, 3), 1)
        		        image.putpixel((3, 3), 1)
                		image.putpixel((4, 3), 1)
		                image.putpixel((7, 3), 1)

			elif hour ==10 or hour == 22:	#ten
       	        		image.putpixel((0, 0), 1)
	                	image.putpixel((5, 0), 1)
	        	        image.putpixel((6, 0), 1)

			elif hour ==11 or hour == 23:	#eleven
                		image.putpixel((2, 1), 1)
	                	image.putpixel((3, 1), 1)
	        	        image.putpixel((6, 1), 1)
        	        	image.putpixel((7, 1), 1)

			else:	#twelve 
        		        image.putpixel((0, 0), 1)
	        	        image.putpixel((1, 0), 1)
        	        	image.putpixel((3, 0), 1)
	                	image.putpixel((7, 0), 1)
		                image.putpixel((7, 1), 1)

			#display 'Heure' - unless displaying version number or count mode
			if (prefix != 'V' and  min != 0 and hour != -1) or prefix == 'T':
			        image.putpixel((3, 4), 1)
			        image.putpixel((4, 4), 1)
			        image.putpixel((5, 4), 1)
		        	image.putpixel((6, 4), 1)
			        image.putpixel((7, 4), 1)


                        # Check for special case - add plural
        	                if hour > 1:	#plural
                	           	image.putpixel((7, 5), 1)


                        if min < 8:
                                pass    

                        elif min < 23:		#et & quarter
				image.putpixel((0, 6), 1)
		                image.putpixel((1, 6), 1)

		                image.putpixel((3, 6), 1)
		                image.putpixel((4, 6), 1)
		                image.putpixel((5, 6), 1)
		                image.putpixel((6, 6), 1)
		                image.putpixel((7, 6), 1)

                        elif min < 38:		#et & half
		                image.putpixel((0, 6), 1)
		                image.putpixel((1, 6), 1)

		                image.putpixel((0, 7), 1)
		                image.putpixel((1, 7), 1)
		                image.putpixel((2, 7), 1)
		                image.putpixel((3, 7), 1)
		                image.putpixel((4, 7), 1)


                        elif min < 53:		#minus & quarter
		                image.putpixel((0, 5), 1)
		                image.putpixel((1, 5), 1)
		                image.putpixel((2, 5), 1)
		                image.putpixel((3, 5), 1)
		                image.putpixel((4, 5), 1)

		                image.putpixel((3, 6), 1)
		                image.putpixel((4, 6), 1)
		                image.putpixel((5, 6), 1)
		                image.putpixel((6, 6), 1)
		                image.putpixel((7, 6), 1)


		# update the output drivers
        	device.display(image)

        # admin displays FRENCH
        # these display the variuos setup and status displays

        def init(self):
		image = Image.new('1', (8, 8))
		image.putpixel((3, 7), 1)
		image.putpixel((5, 7), 1)
		image.putpixel((7, 7), 1)

                # update the output drivers
                device.display(image)

        def error(self):
		image = Image.new('1', (8, 8))
		image.putpixel((3, 3), 1)
		image.putpixel((4, 4), 1)
		image.putpixel((6, 4), 1)
		image.putpixel((7, 4), 1)

                # update the output drivers
                device.display(image)

        def high(self,state):   # display or clear 'H' (Haute)
		image = Image.new('1', (8, 8))

                if state == True:
                        image.putpixel((1, 3), 1)

                else:
                        image.putpixel((1, 3), 0)


                # update the output drivers
                device.display(image)


        def low(self,state):    # display or clear 'F' (Faible)
		image = Image.new('1', (8, 8))

                if state == True:
			image.putpixel((7, 3), 1)
                else:
			image.putpixel((7, 3), 0)


                # update the output drivers
                device.display(image)

	def test(self):		#display the word test to indicate you are entering demo mode
				# should the word 'tester' but cannot fit that in
                image = Image.new('1', (8, 8))
		image.putpixel((7, 2), 1)
		image.putpixel((7, 4), 1)
		image.putpixel((7, 5), 1)
		image.putpixel((7, 6), 1)

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
