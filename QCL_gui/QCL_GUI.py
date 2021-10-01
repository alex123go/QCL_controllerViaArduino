from PyQt5 import QtGui, Qt, QtCore, QtWidgets, uic

import sys
import time

import numpy as np

from comms import QCL_comms

class QCL_GUI(QtWidgets.QWidget):
	def __init__(self):
		super(QCL_GUI, self).__init__()
#
#	
		uic.loadUi("QCL_GUI.ui", self)
		
#		# self.loadInternalParameters()
		self.initUI()
		self.show()
		
		
		self.qcl = QCL_comms()
	
	def closeEvent(self, event):
        
		self.closeSerial()
		
		can_exit = 1
		if can_exit:
			event.accept() # let the window close
		else:
			event.ignore()
	
	def initUI(self):
		self.pushButton_serial_connect.pressed.connect(self.startSerial)
		self.pushButton_serial_disconnect.pressed.connect(self.closeSerial)
		
		self.pushButton_Comb1_power.pressed.connect(lambda: self.powerComb(1))
		self.pushButton_Comb1_enable.pressed.connect(lambda: self.enableComb(1))
		
		self.pushButton_Comb2_power.pressed.connect(lambda: self.powerComb(2))
		self.pushButton_Comb2_enable.pressed.connect(lambda: self.enableComb(2))
		self.updateUI()
		
	def updateUI(self):
		print('TODO')
		
		
	def startSerial(self):
		print('Opening serial port')
		self.qcl.connect(port = 'COM9')
		print('started')
		# arduino reset at serial connection (but why?)
		self.comb_power = [0,0]
		self.comb_enable = [0,0]
		
	def closeSerial(self):
		print('closing serial port')
		self.qcl.disconnect()
		
	def powerComb(self,comb):
		actual_state = self.comb_power[comb-1]
		new_state = int(not(actual_state))
		self.qcl.powerComb(comb, new_state)
		self.comb_power[comb-1] = new_state
		self.updateUI()
		
	def enableComb(self,comb):
		actual_state = self.comb_enable[comb-1]
		new_state = int(not(actual_state))
		self.qcl.enableComb(comb, int(not(actual_state)))
		self.comb_enable[comb-1] = new_state
		self.updateUI()
	

	
if __name__ == '__main__':
	print("main: about to create controller instance")
	
	app = QtCore.QCoreApplication.instance()
	if app is None:
		print("QCoreApplication not running yet. creating.")
		bEventLoopWasRunningAlready = False
		app = QtWidgets.QApplication(sys.argv)
	else:
		bEventLoopWasRunningAlready = True
		print("QCoreApplication already running.")
			
	controller_obj = QCL_GUI()
	
	try:
		app.exec_()
	except Exception as e:
		controller_obj.closeSerial()
		print("Exception during app.exec_():")
		print(e)

	# This code here is to handle weird interaction between IPython's event handler:
	# Depending on the setting for the graphical backend in Spyder (Tools/Preferences/IPython Console/Graphics/Backend = (Automatic or Inline),
	# the Qt event loop might be already running, so the proper way to teardown our application,
	# for example to enable re-using the same console to run another instance afterwards,
#	# is different.
#	if controller_obj.bEventLoopWasRunningAlready == False:
#		# controller_obj.stopCommunication()
#		del controller_obj
