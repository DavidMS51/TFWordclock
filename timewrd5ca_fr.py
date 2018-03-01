#!/usr/bin/env python

# Python Class for use on word clock project  
# Assumes an 8x8 matrix common anode type
# David Saul 2018
# This is configured for the PCB layout REV 4 onwards

# From version 5
# 	Class has changed to use the luma.led_matrix library
# 	This is not compatible with earlier vesions using the max7219 library which is
#	if effectively obsolete from Dec 2017
#
#	Each language has it's own timewrd file in the format timewrd5ca_eng.py
#	This avoids this file getting too ungainly and also makes it easier
#	to add support for other displays in the future
#
#	Support for various status symbol display has changed
#
#
# ++++++++++++++++
# +              +
# +    FRENCH    +
# +              +
# ++++++++++++++++
#
# This class is written to work with the TFWordclock App version 5 and higher

# Because of the change of library some version 4 features are slightly different
# --- the various warnings are now implemented as 'count downs' rather than moving bars


# luma.led_matrix libuary - Richard Hull
# https://github.com/rm-hull/luma.led_matrix
#

from __future__ import print_function, division

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep
from PIL import Image


# French Class
class DMS_wrdck:

	def __init__(self, rotation = 0):
		serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(serial, rotate = rotation)

	def ckdisp(self,min,hour, prefix=False, blink='none'):

		# Perform basic error check on variables
		if min < 0 or min > 59:
			return
		if hour < -1 or hour > 24:
			return

	        # Clear the display first by generating new image
		image = Image.new('1', (8, 8))

		# Display additional character if needed
		if prefix == 'A':		# Display astrix
			image.putpixel((2, 6), 1)
		elif prefix == 'V':		# Display EN and number - to indicate version number
			image.putpixel((4, 7), 1)
			image.putpixel((5, 7), 1)
		else:
			pass

		# Correct from 24 hour to 12
		if hour == 0:
			hour = 1

		# Display minutes past / to the hour in the nearest 15 minute 'slot'

		# Sort out special cases for midnight and midday, but supress for count downs etc
		if min < 8 and prefix == False and hour == 12:
			image.putpixel((0, 5), 1)
			image.putpixel((2, 5), 1)
			image.putpixel((5, 5), 1)
			image.putpixel((6, 5), 1)

		elif min < 8 and prefix == False and hour == 0:
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
				hour = hour + 1
			if hour == 24:
				hour = 1        

			# Display the hours
			if hour == -1: # blank hour display
				pass

			elif hour == 1 or hour == 13:	# one
				image.putpixel((1, 2), 1)
				image.putpixel((2, 3), 1)
				image.putpixel((3, 3), 1)

			elif hour == 2 or hour == 14:	# two
				image.putpixel((0, 0), 1)
				image.putpixel((2, 0), 1)
				image.putpixel((3, 0), 1)
				image.putpixel((6, 0), 1)

			elif hour == 3 or hour == 15:	# three
				image.putpixel((0, 1), 1)
				image.putpixel((1, 1), 1)
				image.putpixel((2, 1), 1)
				image.putpixel((4, 1), 1)
				image.putpixel((5, 1), 1)

			elif hour == 4 or hour == 16:	# four
				image.putpixel((0, 2), 1)
				image.putpixel((1, 2), 1)
				image.putpixel((2, 2), 1)
				image.putpixel((3, 2), 1)
				image.putpixel((4, 2), 1)
				image.putpixel((5, 2), 1)

			elif hour == 5 or hour == 17:	# five
				image.putpixel((0, 3), 1)
				image.putpixel((0, 4), 1)
				image.putpixel((1, 4), 1)
				image.putpixel((2, 4), 1)

			elif hour == 6 or hour == 18:	# six
				image.putpixel((4, 0), 1)
				image.putpixel((5, 0), 1)
				image.putpixel((6, 0), 1)

			elif hour == 7 or hour == 19:	# seven
				image.putpixel((5, 1), 1)
				image.putpixel((5, 2), 1)
				image.putpixel((6, 2), 1)
				image.putpixel((7, 2), 1)

			elif hour == 8 or hour == 20:	# eight
				image.putpixel((1, 3), 1)
				image.putpixel((4, 3), 1)
				image.putpixel((5, 3), 1)
				image.putpixel((6, 3), 1)

			elif hour == 9 or hour == 21:	# nine
				image.putpixel((2, 3), 1)
				image.putpixel((3, 3), 1)
				image.putpixel((4, 3), 1)
				image.putpixel((7, 3), 1)

			elif hour == 10 or hour == 22:	# ten
				image.putpixel((0, 0), 1)
				image.putpixel((5, 0), 1)
				image.putpixel((6, 0), 1)

			elif hour == 11 or hour == 23:	# eleven
				image.putpixel((2, 1), 1)
				image.putpixel((3, 1), 1)
				image.putpixel((6, 1), 1)
				image.putpixel((7, 1), 1)

			else:	# twelve 
				image.putpixel((0, 0), 1)
				image.putpixel((1, 0), 1)
				image.putpixel((3, 0), 1)
				image.putpixel((7, 0), 1)
				image.putpixel((7, 1), 1)

			# Display 'Heure' - unless displaying version number or count mode
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

			elif min < 23:		# et & quarter
				image.putpixel((0, 6), 1)
				image.putpixel((1, 6), 1)

				image.putpixel((3, 6), 1)
				image.putpixel((4, 6), 1)
				image.putpixel((5, 6), 1)
				image.putpixel((6, 6), 1)
				image.putpixel((7, 6), 1)

			elif min < 38:		# et & half
				image.putpixel((0, 6), 1)
				image.putpixel((1, 6), 1)

				image.putpixel((0, 7), 1)
				image.putpixel((1, 7), 1)
				image.putpixel((2, 7), 1)
				image.putpixel((3, 7), 1)
				image.putpixel((4, 7), 1)

			elif min < 53:		# minus & quarter
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

		# Update the output drivers
		self.device.display(image)

        # Admin displays FRENCH
        # These allow the various setup and status displays to be
	# language specific without need to change the main code

	def init(self):
		image = Image.new('1', (8, 8))
		image.putpixel((3, 7), 1)
		image.putpixel((5, 7), 1)
		image.putpixel((7, 7), 1)

		# Update the output drivers
		self.device.display(image)

	def error(self):
		image = Image.new('1', (8, 8))
		image.putpixel((3, 3), 1)
		image.putpixel((4, 4), 1)
		image.putpixel((6, 4), 1)
		image.putpixel((7, 4), 1)

		# Update the output drivers
		self.device.display(image)

	def high(self,state):   # Display or clear 'H' (Haute)
		image = Image.new('1', (8, 8))
		if state == True:
			image.putpixel((1, 3), 1)
		else:
			image.putpixel((1, 3), 0)

		# Update the output drivers
		self.device.display(image)


	def low(self,state):    # Display or clear 'F' (Faible)
		image = Image.new('1', (8, 8))
		if state == True:
			image.putpixel((7, 3), 1)
		else:
			image.putpixel((7, 3), 0)

		# Update the output drivers
		self.device.display(image)

	def test(self):		# Display the word TEST to indicate you are entering demo mode
				# Should be the word 'tester' but cannot fit that in
		image = Image.new('1', (8, 8))
		image.putpixel((7, 2), 1)
		image.putpixel((7, 4), 1)
		image.putpixel((7, 5), 1)
		image.putpixel((7, 6), 1)

		# Update the output drivers
		self.device.display(image)

	def align(self):	# Display alignment screen
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

		# Update the output drivers
		self.device.display(image)

	def pixel(self,x,y):		# Allows external app to set an individual pixel
		image = Image.new('1', (8, 8))
		image.putpixel((x, y), 1)

		# Update the output drivers
		self.device.display(image)

	def clear(self):		# Clear the current display
		image = Image.new('1', (8, 8))
		# Update the output drivers
		self.device.display(image)

	def contrast(self,level):	# Set the brightness level
		if level > 255 or level < 0:
			return
		self.device.contrast(level)
