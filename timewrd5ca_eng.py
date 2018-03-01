#!/usr/bin/env python

# Python Class for use on word clock project
# Assumes an 8x8 matrix common anode type
# David Saul 2018
# This is configured for the PCB layout REV 4 onwards

# From version 5
# 	Class has changed to use the luma.led_matrix library
# 	This is not compatible with earlier versions using the max7219 library which is
#	effectcivly obsolete from Dec 2017
#
#	Each language has it's own timewrd file in the format timewrd5ca_eng.py
#	This avoids this file getting too ungainly and also makes it easier
#	to add support for other displays in the future
#
#	Support for various status symbol displays has changed
#
#
# +++++++++++++++
# +             +
# +   ENGLISH   +
# +             +
# +++++++++++++++
#
# This class is written to work with the TFWordclock App version 5 and higher

# Because of the change of libuary some version 4 features are slightly different
# --- the various warning are now implemented as 'count downs' rather than moving bars


# luma.led_matrix libuary - Richard Hull
# https://github.com/rm-hull/luma.led_matrix
#

from __future__ import print_function, division

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep
from PIL import Image


# English Class
class DMS_wrdck:

	def __init__(self, rotation = 0):
		serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(serial, rotate = rotation)

	def ckdisp(self,mint,hour, prefix=False, blink='none'):

		# Perfor basic error check on variables
		if mint < 0 or mint > 59:
			return
		if hour < -1 or hour > 24:
			return

		# Clear the display first by generating new image

		image = Image.new('1', (8, 8))

		# Display additional charater if needed
		if prefix == 'A':		# Display astrix
			image.putpixel((2, 2), 1)
		elif prefix == 'V':		# Display V - to indicate version number
			image.putpixel((3, 1), 1)
		else:
			pass

		# Convert minutes into 5 minute slots, with true rounding if no minute blinking
		if blink == 'none':
			min = int(round(mint / 5.0))
		else:
			min = mint // 5

		# Increment 'hour' for > 30 mins past the hour
		if min > 6 and hour != -1:	# Except for special case when hour is inhibited
			hour = hour + 1
			if hour == 24:
				hour = 12

		# Correct from 24 hour to 12
		if hour == 0:
			hour = 12

		if hour > 12:
			hour = hour - 12

		# Correct for final 2/3 minutes in the hour (only used when no minute blinking)
		if min == 12:
			min = 0

		if blink == 'off':
			if min == 0:
				hour = -1
			else:
				min = 0

		# Display minutes past / to the hour in to nearest 5 minute 'slot'
		if min == 0:	# oclock
			pass

		elif min == 1:	# five_past
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 2:	# ten_past
			image.putpixel((4, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 3:	# fifteen_past
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 4:	# tweny_past
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 5:	# twenty5_past
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 6:	# half_past
			image.putpixel((0, 0), 1)
			image.putpixel((1, 0), 1)
			image.putpixel((0, 2), 1)
			image.putpixel((1, 2), 1)
			image.putpixel((3, 2), 1)
			image.putpixel((4, 2), 1)
			image.putpixel((5, 2), 1)
			image.putpixel((6, 2), 1)

		elif min == 7:	# twenty5_to
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min == 8:	# twenty_to
			image.putpixel((2, 0), 1)
			image.putpixel((3, 0), 1)
			image.putpixel((4, 0), 1)
			image.putpixel((5, 0), 1)
			image.putpixel((6, 0), 1)
			image.putpixel((7, 0), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min == 9:	# fifteen_to
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((2, 1), 1)
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		elif min == 10:	# ten_to
			image.putpixel((4, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((7, 1), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		else:	# five_to
			image.putpixel((0, 1), 1)
			image.putpixel((1, 1), 1)
			image.putpixel((3, 1), 1)
			image.putpixel((5, 1), 1)
			image.putpixel((6, 2), 1)
			image.putpixel((7, 2), 1)

		# Display the hours
		if hour == -1: # blank hour display
			pass

		elif hour == 1:		# one
			image.putpixel((0, 4), 1)
			image.putpixel((1, 4), 1)
			image.putpixel((2, 4), 1)

		elif hour == 2:		# two
			image.putpixel((0, 5), 1)
			image.putpixel((1, 5), 1)
			image.putpixel((1, 6), 1)

		elif hour == 3:		# three
			image.putpixel((3, 4), 1)
			image.putpixel((4, 4), 1)
			image.putpixel((5, 4), 1)
			image.putpixel((6, 4), 1)
			image.putpixel((7, 4), 1)

		elif hour == 4:		# four
			image.putpixel((0, 6), 1)
			image.putpixel((1, 6), 1)
			image.putpixel((2, 6), 1)
			image.putpixel((3, 6), 1)

		elif hour == 5:		# five
			image.putpixel((4, 6), 1)
			image.putpixel((5, 6), 1)
			image.putpixel((6, 6), 1)
			image.putpixel((7, 6), 1)

		elif hour == 6:		# six
			image.putpixel((0, 7), 1)
			image.putpixel((1, 7), 1)
			image.putpixel((2, 7), 1)

		elif hour == 7:		# seven
			image.putpixel((3, 7), 1)
			image.putpixel((4, 7), 1)
			image.putpixel((5, 7), 1)
			image.putpixel((6, 7), 1)
			image.putpixel((7, 7), 1)

		elif hour == 8:		# eight
			image.putpixel((3, 3), 1)
			image.putpixel((4, 3), 1)
			image.putpixel((5, 3), 1)
			image.putpixel((6, 3), 1)
			image.putpixel((7, 3), 1)

		elif hour == 9:		# nine
			image.putpixel((0, 3), 1)
			image.putpixel((1, 3), 1)
			image.putpixel((2, 3), 1)
			image.putpixel((3, 3), 1)

		elif hour == 10:	# ten
			image.putpixel((7, 3), 1)
			image.putpixel((7, 4), 1)
			image.putpixel((7, 5), 1)

		elif hour == 11:	# eleven
			image.putpixel((2, 5), 1)
			image.putpixel((3, 5), 1)
			image.putpixel((4, 5), 1)
			image.putpixel((5, 5), 1)
			image.putpixel((6, 5), 1)
			image.putpixel((7, 5), 1)

		else:	# twelve
			image.putpixel((0, 5), 1)
			image.putpixel((1, 5), 1)
			image.putpixel((2, 5), 1)
			image.putpixel((3, 5), 1)
			image.putpixel((5, 5), 1)
			image.putpixel((6, 5), 1)

		# Update the output drivers
		self.device.display(image)

	# Admin displays ENGLISH
	# These allow the various setup and status displays to be
	# language specific without need to change the main code        

	def init(self):		# Display 'INIT'
		image = Image.new('1', (8, 8))
		image.putpixel((1, 3), 1)
		image.putpixel((2, 3), 1)
		image.putpixel((4, 3), 1)
		image.putpixel((7, 3), 1)

		# Update the output drivers
		self.device.display(image)

	def error(self):	# Display 'E E E'
		image = Image.new('1', (8, 8))
		image.putpixel((2, 5), 1)
		image.putpixel((4, 5), 1)
		image.putpixel((6, 5), 1)

		# Update the output drivers
		self.device.display(image)

	def high(self,state):   # Display or clear 'H'
		image = Image.new('1', (8, 8))
		if state == True:
			image.putpixel((0, 0), 1)
		else:
			image.putpixel((0, 0), 0)

		# Update the output drivers
		self.device.display(image)


	def low(self,state):    # Display or clear 'L'
		image = Image.new('1', (8, 8))
		if state == True:       
			image.putpixel((0, 2), 1)
		else:
			image.putpixel((0, 2), 0)

		# Update the output drivers
		self.device.display(image)

	def test(self):		# Display the word TEST to indicate you are entering demo mode
		image = Image.new('1', (8, 8))
		image.putpixel((4, 1), 1)
		image.putpixel((5, 1), 1)
		image.putpixel((5, 2), 1)
		image.putpixel((6, 2), 1)

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
