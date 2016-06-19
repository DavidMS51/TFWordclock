#!/usr/bin/env python

# Python Class for use on word clock project  - Multi Langauge  Version
# Assumes and 8x8 matrix common anode type
# David Saul 2016
# This is configured for the PCB layout REV 4 onwards

# max7219 libuary Copyright 2015, Richard Hull
# https://github.com/rm-hull
# see http://max7219.readthedocs.org/index.html, for max7219.led documentaion

import max7219.led as led
import math


#English Class
class DMS_wrdck_en:

        def lan(self):
                lan =  "English langauge class loaded"
		return lan

	device = led.matrix(cascaded=1)

	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
		self.device.pixel(0, 4, 1, redraw=False)
		self.device.pixel(1, 4, 1, redraw=False)
		self.device.pixel(2, 4, 1, redraw=False)

	def two(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(1, 6, 1, redraw=False)

	def three(self):
		self.device.pixel(3, 4, 1, redraw=False)
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)

	def four(self):
		self.device.pixel(0, 6, 1, redraw=False)
		self.device.pixel(1, 6, 1, redraw=False)
		self.device.pixel(2, 6, 1, redraw=False)
		self.device.pixel(3, 6, 1, redraw=False)

	def five(self):
		self.device.pixel(4, 6, 1, redraw=False)
		self.device.pixel(5, 6, 1, redraw=False)
		self.device.pixel(6, 6, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)

	def six(self):
		self.device.pixel(0, 7, 1, redraw=False)
		self.device.pixel(1, 7, 1, redraw=False)
		self.device.pixel(2, 7, 1, redraw=False)

	def seven(self):
		self.device.pixel(3, 7, 1, redraw=False)
		self.device.pixel(4, 7, 1, redraw=False)
		self.device.pixel(5, 7, 1, redraw=False)
		self.device.pixel(6, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)

	def eight(self):
		self.device.pixel(3, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(5, 3, 1, redraw=False)
		self.device.pixel(6, 3, 1, redraw=False)
		self.device.pixel(7, 3, 1, redraw=False)

	def nine(self):
		self.device.pixel(0, 3, 1, redraw=False)
		self.device.pixel(1, 3, 1, redraw=False)
		self.device.pixel(2, 3, 1, redraw=False)
		self.device.pixel(3, 3, 1, redraw=False)

	def ten(self):
		self.device.pixel(7, 3, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)

	def eleven(self):
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(3, 5, 1, redraw=False)
		self.device.pixel(4, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(6, 5, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)

	def twelve(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(3, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(6, 5, 1, redraw=False)


	def oclock(self):	# blank no minute displayed
		pass		# pass is like nop in machine code 
	
	def five_past(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)


	def ten_past(self):
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

	def fifteen_past(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

 	def twenty_past(self):
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

	def twenty5_past(self):
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

	def half_past(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(1, 0, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)

	def twenty5_to(self):
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def twenty_to(self):
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def fifteen_to(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def ten_to(self):
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def five_to(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	# Display the hours
	def hour(self,hour):
                if hour <0 or hour >24:
                        return

		pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
                self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,\
                self.one,self.two,self.three,self.four,self.five,\
                self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
                pointer[hour]()


	# admin displays ENGLISH
        # these allow the variuos setup and status displays to be
        # language specific without need to change the main code        

        def astrix(self,state):  # display or clear astrix
		if state == True:	
	                self.device.pixel(2, 2, 1, redraw=True)
		else:
			self.device.pixel(2, 2, 0, redraw=True)

        def init(self):
                self.device.pixel(1, 3, 1, redraw=False)
                self.device.pixel(2, 3, 1, redraw=False)
                self.device.pixel(4, 3, 1, redraw=False)
                self.device.pixel(7, 3, 1, redraw=False)

                # update the output drivers
                self.device.flush()

        def error(self):
                self.device.pixel(2, 5, 1, redraw=False)
                self.device.pixel(4, 5, 1, redraw=False)
                self.device.pixel(6, 5, 1, redraw=False)

                # update the output drivers
                self.device.flush()

	def high(self,state):	# display or clear 'H'
		if state == True:
			self.device.pixel(0,0,1, redraw=True)
		else:
			self.device.pixel(0,0,0, redraw=True)

	def low(self,state):	# display or clear 'L'
		if state == True:	
	                self.device.pixel(0,2,1, redraw=True)
		else:
			self.device.pixel(0,2,0, redraw=True)

			

        def ver(self,rev):              # this is the odd one as it needs a value
                                        # display EN and rev number
                if rev > 12 or rev < 1: # basic syntax check
                        return
                self.device.pixel(3, 1, 1, redraw=False)
                self.hour(rev)          # use hour sub to displat revision

                # update the output drivers
                self.device.flush()


	
	def ckdisp(self,mint,hour):

		# Perfor basic error check on variables
               	if mint < 0 or mint > 59:
                        return
               	if hour < -1 or hour > 24:
                        return

		#correct from 24 hour to 12
                if hour == 0:
                        hour =12


		# Clear the display first
		self.device.clear(0)

		# Convert minutes into 5 minute slots
                mint = float(mint)
                mint = mint / 5
                tmp = math.modf(mint)
                if tmp[0] < 0.5:
                        min = int(tmp[1])
                else:
                        min = int(tmp[1]+1)

		# add incrument 'hour' for >30 mins past the hour
		if min > 6:
			hour = hour +1
			if hour == 24:
				hour = 12	

		# Bodge to keep display correct for the last 3 minutes before the hour
                if min == 12:
                        min = 0

		# bodge to blank hours display during minute setup
		# if hour = -1 force it to 0 so it does not display
		if hour == -1:
			hour = 0

#		print "min lookup ",min		# for debug only
	
		# Display miuntes past / to the hour in to nearest 5 minute 'slot'
		pointerm = [self.oclock,self.five_past,self.ten_past,self.fifteen_past,\
		self.twenty_past,self.twenty5_past,self.half_past,self.twenty5_to,\
		self.twenty_to,self.fifteen_to,self.ten_to,self.five_to]
                pointerm[min]()

#               print "sub ",hour,":", min              #For debug only

		# Display the hours
		self.hour(hour)

		# update the output drivers
                self.device.flush()
#------------------------------------------------------------------------------------------------

#French Class
class DMS_wrdck_fn:

	device = led.matrix(cascaded=1)

	def lan(self):
		lan =  "French langauge class loaded"
		return lan

#	device = led.matrix(cascaded=1)



	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 3, 1, redraw=False)
		self.device.pixel(3, 3, 1, redraw=False)

	def two(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)

	def three(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)


	def four(self):
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
          	self.device.pixel(4, 2, 1, redraw=False)
                self.device.pixel(5, 2, 1, redraw=False)


	def five(self):
		self.device.pixel(0, 3, 1, redraw=False)
		self.device.pixel(0, 4, 1, redraw=False)
		self.device.pixel(1, 4, 1, redraw=False)
		self.device.pixel(2, 4, 1, redraw=False)

	def six(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)

	def seven(self):
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def eight(self):
		self.device.pixel(1, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(5, 3, 1, redraw=False)
		self.device.pixel(6, 3, 1, redraw=False)


	def nine(self):
		self.device.pixel(2, 3, 1, redraw=False)
		self.device.pixel(3, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(7, 3, 1, redraw=False)

	def ten(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)

	def eleven(self):
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
                self.device.pixel(7, 1, 1, redraw=False)


	def twelve(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(1, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)


	def oclock(self):	# blank no minute displayed
		pass		# pass is like nop in machine code 
	
	def quarter(self):
		self.device.pixel(3, 6, 1, redraw=False)
		self.device.pixel(4, 6, 1, redraw=False)
		self.device.pixel(5, 6, 1, redraw=False)
		self.device.pixel(6, 6, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)


	def half(self):
		self.device.pixel(0, 7, 1, redraw=False)
		self.device.pixel(1, 7, 1, redraw=False)
		self.device.pixel(2, 7, 1, redraw=False)
		self.device.pixel(3, 7, 1, redraw=False)
		self.device.pixel(4, 7, 1, redraw=False)


	def minus(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(3, 5, 1, redraw=False)
		self.device.pixel(4, 5, 1, redraw=False)

 	def midnight(self):
		self.device.pixel(2, 7, 1, redraw=False)
		self.device.pixel(3, 7, 1, redraw=False)
		self.device.pixel(5, 7, 1, redraw=False)
		self.device.pixel(6, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)

	def midday(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(6, 5, 1, redraw=False)

	def Heure(self):
		self.device.pixel(3, 4, 1, redraw=False)
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)

	def S(self):
                self.device.pixel(7, 5, 1, redraw=False)

	def et(self):
		self.device.pixel(0, 6, 1, redraw=False)
		self.device.pixel(1, 6, 1, redraw=False)

	# Display the hours - call with int between 0 and 24
	def hour(self,hour):
		if hour <0 or hour >24:
			return

		pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
		self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,\
		self.one,self.two,self.three,self.four,self.five,\
		self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
		pointer[hour]()


	# admin displays FRENCH
	# these allow the variuos setup and status displays to be
	# language specific without need to change the main code	

	def astrix(self,state):	#display or clear astrix
		if state == True:
			self.device.pixel(2, 6, 1, redraw=True)
		else:
			self.device.pixel(2, 6, 0, redraw=True)

	def init(self):
		self.device.pixel(3, 7, 1, redraw=False)
                self.device.pixel(5, 7, 1, redraw=False)
                self.device.pixel(7, 7, 1, redraw=False)

		# update the output drivers
                self.device.flush()

	def error(self):
                self.device.pixel(3, 3, 1, redraw=False)
                self.device.pixel(4, 4, 1, redraw=False)
                self.device.pixel(6, 4, 1, redraw=False)
                self.device.pixel(7, 4, 1, redraw=False)

		# update the output drivers
                self.device.flush()

	def high(self,state):   # display or clear 'H - haute'      
                if state == True:
                        self.device.pixel(1,3,1, redraw=True)
                else:
                        self.device.pixel(1,3,0, redraw=True)

        def low(self,state):    # display or clear 'L - faible'
                if state == True:
                        self.device.pixel(7,3,1, redraw=True)
                else:
                        self.device.pixel(7,3,0, redraw=True)



	def ver(self,rev):		# this is the odd one as it needs a value
					# display EN and rev number
		if rev > 12 or rev < 1: # basic syntax check
			return
		self.device.pixel(4, 7, 1, redraw=False)
                self.device.pixel(5, 7, 1, redraw=False)
		self.hour(rev)		# use hour sub to displat revision			

		# update the output drivers
                self.device.flush()
	
	def ckdisp(self,min,hour):

		# Perfor basic error check on variables
               	if min < 0 or min > 59:
                        return
               	if hour < 0 or hour > 23:
                        return

		#correct from 24 hour to 12
		if hour == 0:
			hour =1

#		print "sub ",hour,":", min		#For debug only

		# Clear the display first
		self.device.clear(0)

		#Sort out special cases for midnight and midday
		if min < 8 and hour == 12:
			self.midday()
		elif min < 8 and  hour == 0:
			self.midnight()
		elif min > 52 and hour == 11:
                        self.midday()
                elif min > 52 and hour == 23:
                        self.midnight()
	
		#Everything else - hours
		else:	
					
			# add incrument 'hour' for >30 mins past the hour
			if min > 38:
				hour = hour +1
				if hour == 24:
					hour = 1	


			# Display the hours
			self.hour(hour)

			#display Heure
			self.Heure()
		
			#check for special case	- add plural			
			if hour == 1:
				self.S()

			if min < 8:
				pass	

			elif min < 23:
				self.et()
				self.quarter()

			elif min < 38:
				self.et()
                                self.half()

			elif min < 53:
				self.et()
				self.minus()
				self.quarter()

		# update the output drivers
                self.device.flush()

#------------------------------------------------------------------------------------------------

#Dutch Class
class DMS_wrdck_du:

        device = led.matrix(cascaded=1)

        def lan(self):
                lan =  "Dutch langauge class loaded"
                return lan


	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)

	def two(self):
		self.device.pixel(3, 4, 1, redraw=False)
		self.device.pixel(4, 4, 1, redraw=False)
		self.device.pixel(5, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)

	def three(self):
		self.device.pixel(4, 6, 1, redraw=False)
		self.device.pixel(5, 6, 1, redraw=False)
		self.device.pixel(6, 6, 1, redraw=False)
		self.device.pixel(7, 6, 1, redraw=False)

	def four(self):
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(6, 5, 1, redraw=False)

	def five(self):
		self.device.pixel(1, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(3, 5, 1, redraw=False)
		self.device.pixel(4, 5, 1, redraw=False)

	def six(self):
		self.device.pixel(0, 3, 1, redraw=False)
		self.device.pixel(1, 3, 1, redraw=False)
		self.device.pixel(2, 3, 1, redraw=False)

	def seven(self):
		self.device.pixel(3, 3, 1, redraw=False)
		self.device.pixel(4, 3, 1, redraw=False)
		self.device.pixel(5, 3, 1, redraw=False)
		self.device.pixel(6, 3, 1, redraw=False)
		self.device.pixel(7, 3, 1, redraw=False)

	def eight(self):
		self.device.pixel(0, 6, 1, redraw=False)
		self.device.pixel(1, 6, 1, redraw=False)
		self.device.pixel(2, 6, 1, redraw=False)
		self.device.pixel(3, 6, 1, redraw=False)


	def nine(self):
		self.device.pixel(0, 4, 1, redraw=False)
		self.device.pixel(1, 4, 1, redraw=False)
		self.device.pixel(2, 4, 1, redraw=False)
		self.device.pixel(6, 4, 1, redraw=False)
		self.device.pixel(7, 4, 1, redraw=False)

	def ten(self):
		self.device.pixel(0, 5, 1, redraw=False)
		self.device.pixel(2, 5, 1, redraw=False)
		self.device.pixel(5, 5, 1, redraw=False)
		self.device.pixel(7, 5, 1, redraw=False)


	def eleven(self):
		self.device.pixel(0, 7, 1, redraw=False)
		self.device.pixel(1, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)

	def twelve(self):
		self.device.pixel(2, 7, 1, redraw=False)
		self.device.pixel(3, 7, 1, redraw=False)
		self.device.pixel(4, 7, 1, redraw=False)
		self.device.pixel(5, 7, 1, redraw=False)
		self.device.pixel(6, 7, 1, redraw=False)
		self.device.pixel(7, 7, 1, redraw=False)


	def oclock(self):	# blank no minute displayed
		pass		# pass is like nop in machine code 
	
	def five_past(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)


	def ten_past(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)


	def fifteen_past(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(1, 0, 1, redraw=False)
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)

 	def twenty_past(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def twenty5_past(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def half_past(self):
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def twenty5_to(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)

	def twenty_to(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(4, 1, 1, redraw=False)
		self.device.pixel(5, 1, 1, redraw=False)
		self.device.pixel(6, 1, 1, redraw=False)
		self.device.pixel(7, 1, 1, redraw=False)
		self.device.pixel(4, 2, 1, redraw=False)
		self.device.pixel(5, 2, 1, redraw=False)
		self.device.pixel(6, 2, 1, redraw=False)
		self.device.pixel(7, 2, 1, redraw=False)


	def fifteen_to(self):
		self.device.pixel(0, 0, 1, redraw=False)
		self.device.pixel(1, 0, 1, redraw=False)
		self.device.pixel(2, 0, 1, redraw=False)
		self.device.pixel(3, 0, 1, redraw=False)
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)



	def ten_to(self):
		self.device.pixel(4, 0, 1, redraw=False)
		self.device.pixel(5, 0, 1, redraw=False)
		self.device.pixel(6, 0, 1, redraw=False)
		self.device.pixel(7, 0, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)


	def five_to(self):
		self.device.pixel(0, 1, 1, redraw=False)
		self.device.pixel(1, 1, 1, redraw=False)
		self.device.pixel(2, 1, 1, redraw=False)
		self.device.pixel(3, 1, 1, redraw=False)
		self.device.pixel(0, 2, 1, redraw=False)
		self.device.pixel(1, 2, 1, redraw=False)
		self.device.pixel(2, 2, 1, redraw=False)
		self.device.pixel(3, 2, 1, redraw=False)
        # Display the hours
        def hour(self,hour):
                if hour <0 or hour >24:
                        return

                pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
                self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,\
                self.one,self.two,self.three,self.four,self.five,\
                self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
                pointer[hour]()


        # admin displays DUTCH
        # these allow the variuos setup and status displays to be
        # language specific without need to change the main code        

        def astrix(self,state):	 # set / hide astrix
		if state == True:
	                self.device.pixel(2, 2, 1, redraw=True)
		else:
			self.device.pixel(2, 2, 0, redraw=True)

                # update the output drivers
                self.device.flush()

        def init(self):
                self.device.pixel(5, 0, 1, redraw=False)
                self.device.pixel(7, 0, 1, redraw=False)

                # update the output drivers
                self.device.flush()

        def error(self):
                self.device.pixel(3, 1, 1, redraw=False)
                self.device.pixel(4, 1, 1, redraw=False)

                # update the output drivers
                self.device.flush()

	def high(self,state):   # display or clear 'H - hoog '      
                if state == True:
                        self.device.pixel(4,2,1, redraw=True)
                else:
                        self.device.pixel(4,2,0, redraw=True)

        def low(self,state):    # display or clear 'L - Laag'
                if state == True:
                        self.device.pixel(6,2,1, redraw=True)
                else:
                        self.device.pixel(6,2,0, redraw=True)



        def ver(self,rev):              # this is the odd one as it needs a value
                                        # display EN and rev number
                if rev > 12 or rev < 1: # basic syntax check
                        return
                self.device.pixel(0, 1, 1, redraw=False)
                self.device.pixel(6, 1, 1, redraw=False)
                self.device.pixel(7, 1, 1, redraw=False)

                self.hour(rev)          # use hour sub to displat revision

                # update the output drivers
                self.device.flush()


	
	def ckdisp(self,mint,hour):

		# Perfor basic error check on variables
               	if mint < 0 or mint > 59:
                        return
               	if hour < -1 or hour > 23:
                        return

		# Clear the display first
		self.device.clear(0)

		# Convert minutes into 5 minute slots
                mint = float(mint)
                mint = mint / 5
                tmp = math.modf(mint)
                if tmp[0] < 0.5:
                        min = int(tmp[1])
                else:
                        min = int(tmp[1]+1)

		# add incrument 'hour' for >30 mins past the hour
		if min > 3:
			hour = hour +1
			if hour == 24:
				hour = 1	

		# Bodge to keep display correct for the last 3 minutes before the hour
                if min == 12:
                        min = 0

		# bodge to blank hours display during minute setup
                # if hour = -1 force it to 0 so it does not display
                if hour == -1:
                        hour = 0


#		print "min lookup ",min		# for debug only
	
		# Display miuntes past / to the hour in to nearest 5 minute 'slot'
                pointerm = [self.oclock,self.five_past,self.ten_past,self.fifteen_past,\
		self.twenty_past,self.twenty5_past,self.half_past,self.twenty5_to,\
		self.twenty_to,self.fifteen_to,self.ten_to,self.five_to]
                pointerm[min]()
	
#		print "hour lookup ", hour	# for debug only

		# Display the hours
		self.hour(hour)

		# update the output drivers
                self.device.flush()

#----------------------------------------------------------------------------------------------

		

