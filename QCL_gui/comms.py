# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:34:40 2021

@author: Alex1
"""

import serial
import time


class QCL_comms():
	"""docstring for QCL_comms"""
	def __init__(self, arg=None):
		super(QCL_comms, self).__init__()
		self.arg = arg

		self.serActive = False

	def connect(self,port = 'COM9'):
		self.ser = serial.Serial(port,57600)

		# don't know if useful
		self.ser.parity=serial.PARITY_ODD
		self.ser.stopbits=serial.STOPBITS_ONE
		self.ser.bytesize=serial.EIGHTBITS

		# let time for bootloader
		time.sleep(1)
		self.serActive = True

	def disconnect(self):
		if self.serActive == True:
			self.ser.close()
		self.serActive = False

	def sendCmd(self,cmd):
		cmd = cmd + '\n'
		self.ser.write(cmd.encode())
		time.sleep(0.1)

	def powerComb(self,comb='1',status = 0):
		cmd = 'Power'+str(comb)+':'+str(status)
		self.sendCmd(cmd)

	def enableComb(self,comb='1',status = 0):
		cmd = 'Enable'+str(comb)+':'+str(status)
		self.sendCmd(cmd)
