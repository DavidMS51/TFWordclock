
#!/usr/bin/env python

# Python Class for use on Latin version word clock project
# Assumes and 8x8 matrix common anode type
# David Saul 2016
# This is configured for the PCB layout REV 4 onwards

# max7219 libuary Copyright 2015, Richard Hull
# https://github.com/rm-hull
# see http://max7219.readthedocs.org/index.html, for max7219.led documentaion

import max7219.led as led
import math

class DMS_wrdck:

	device = led.matrix(cascaded=1)

	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)

	def two(self):
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

	def three(self):
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)


	def four(self):
		self.device.pixel(0, 3, 1, redraw=False)
		self.device.pixel(1, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(5, 3, 1, redraw=False)
		self.device.pixel(6, 3, 1, redraw=False)
		self.device.pixel(7, 3, 1, redraw=False)


	def five(self):
		self.device.pixel(0, 3, 1, redraw=False)
		self.device.pixel(1, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(5, 3, 1, redraw=False)
		self.device.pixel(7, 3, 1, redraw=False)


	def six(self):
		self.device.pixel(0, 7, 1, redraw=False)
		self.device.pixel(1, 7, 1, redraw=False)
		self.device.pixel(2, 7, 1, redraw=False)
		self.device.pixel(4, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)


	def seven(self):
		self.device.pixel(0, 7, 1, redraw=False)
		self.device.pixel(1, 7, 1, redraw=False)
		self.device.pixel(3, 7, 1, redraw=False)
		self.device.pixel(4, 7, 1, redraw=False)
		self.device.pixel(5, 7, 1, redraw=False)
		self.device.pixel(6, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)

	def eight(self):
		self.device.pixel(0, 6, 1, redraw=False)
		self.device.pixel(1, 6, 1, redraw=False)
		self.device.pixel(2, 6, 1, redraw=False)
		self.device.pixel(3, 6, 1, redraw=False)
		self.device.pixel(6, 6, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)

	def nine(self):
		self.device.pixel(4, 6, 1, redraw=False)
		self.device.pixel(5, 6, 1, redraw=False)
		self.device.pixel(6, 6, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)

	def ten(self):
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)


	def eleven(self):
		self.device.pixel(1, 4, 1, redraw=False)
		self.device.pixel(2, 4, 1, redraw=False)
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)


	def twelve(self):
		self.device.pixel(0, 4, 1, redraw=False)
		self.device.pixel(1, 4, 1, redraw=False)
		self.device.pixel(3, 4, 1, redraw=False)
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)



	def hora(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)

	
	def est(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(1, 0, 1, redraw=False)
		self.device.pixel(2, 0, 1, redraw=False)


	def vigilia(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(3, 5, 1, redraw=False)
		self.device.pixel(4, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(6, 5, 1, redraw=False)

	
	def ckdisp(self,hour):

		# Perfor basic error check on variables - assumes 24 hour clock
               	if hour < 0 or hour > 24:
                        return

		# Clear the display first
		self.device.clear(0)

		self.est()			# always display EST

		if hour > 18 and hour < 22:	# first watch
			self.vigilia()
			self.one()
		elif hour > 21 or hour < 1: 	# second watch
                        self.vigilia()
                        self.two()
		elif hour > 0 and hour < 4:     # third watch
                        self.vigilia()
                        self.three()
		elif hour > 3 and hour < 7:     # fouth watch
                        self.vigilia()
                        self.four()

		else:
			hour = hour - 6		# shift hour to make 7am first hour
			
			self.hora()		# hour

			# Display day the hours
	                pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
			self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
                	pointer[hour]()

		# update the output drivers
                self.device.flush()



		

