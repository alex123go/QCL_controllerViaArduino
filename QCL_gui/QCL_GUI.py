from PyQt5 import QtGui, Qt, QtCore, QtWidgets, uic

import sys
import time
import serial.tools.list_ports


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
		self.pushButton_serial_connect.setEnabled(False)
		self.pushButton_serial_disconnect.pressed.connect(self.closeSerial)
		self.pushButton_serial_disconnect.setEnabled(False)

		self.pushButton_Comb1_power.pressed.connect(self.powerComb1)
		self.pushButton_Comb1_enable.pressed.connect(self.enableComb1)
		
		self.pushButton_Comb2_power.pressed.connect(self.powerComb2)
		self.pushButton_Comb2_enable.pressed.connect(self.enableComb2)

		self.Comb1_setPoint.setText('NA mA') # Not yet implemented
		self.Comb1_current.setText('NA mA')
		self.Comb2_setPoint.setText('NA mA')
		self.Comb2_current.setText('NA mA')
		
		self.disableUI_QCL()
		self.updateSerialList()
		
	def updateUI(self):
		print('TODO') # should implement a way to read digitalOutput in the arduino

	def updateSerialList(self):
		self.comboPorts.clear()
		self.Port_list = self.getSerialList()
		
		if len(self.Port_list) == 0:
			text = 'No serial port available'
			self.comboPorts.addItem(text)
			self.pushButton_serial_connect.setEnabled(False)
		else:
			for i in range(len(self.Port_list)):
				self.comboPorts.addItem(self.Port_list[i])
			self.pushButton_serial_connect.setEnabled(True)


	def getSerialList(self):
		comlist = serial.tools.list_ports.comports()
		connected = []
		for element in comlist:
		    connected.append(element.device)
		return connected

	def disableUI_QCL(self):
		self.pushButton_Comb1_power.setEnabled(False)
		self.pushButton_Comb1_enable.setEnabled(False)
		self.pushButton_Comb2_power.setEnabled(False)
		self.pushButton_Comb2_enable.setEnabled(False)

		self.pushButton_serial_connect.setEnabled(True)
		self.pushButton_serial_disconnect.setEnabled(False)
		self.comboPorts.setEnabled(True)

		self.pushButton_Comb1_power.setText('Turn power ON')
		self.pushButton_Comb1_enable.setText('Enable output')
		self.pushButton_Comb2_power.setText('Turn power ON')
		self.pushButton_Comb2_enable.setText('Enable output')
		self.pushButton_Comb1_power.setStyleSheet('')
		self.pushButton_Comb1_enable.setStyleSheet('')
		self.pushButton_Comb2_power.setStyleSheet('')
		self.pushButton_Comb2_enable.setStyleSheet('')

	def enableUI_QCL(self):
		self.pushButton_Comb1_power.setEnabled(True)
		self.pushButton_Comb1_enable.setEnabled(True)
		self.pushButton_Comb2_power.setEnabled(True)
		self.pushButton_Comb2_enable.setEnabled(True)

		self.pushButton_serial_connect.setEnabled(False)
		self.pushButton_serial_disconnect.setEnabled(True)
		self.comboPorts.setEnabled(False)

		# since we know that the output reset to 0 when we reconnect (maybe use updateUI in the future)
		self.pushButton_Comb1_power.setText('Turn power ON')
		self.pushButton_Comb1_enable.setText('Enable output')
		self.pushButton_Comb2_power.setText('Turn power ON')
		self.pushButton_Comb2_enable.setText('Enable output')
		self.pushButton_Comb1_power.setStyleSheet('background-color: red')
		self.pushButton_Comb1_enable.setStyleSheet('background-color: red')
		self.pushButton_Comb2_power.setStyleSheet('background-color: red')
		self.pushButton_Comb2_enable.setStyleSheet('background-color: red')
		
	def startSerial(self):
		print('Opening serial port')
		index = self.comboPorts.currentIndex()
		port = self.Port_list[index]
		print(port)
		self.qcl.connect(port = port)
		# arduino reset GPIO at serial connection
		self.comb_power = [0,0]
		self.comb_enable = [0,0]
		self.enableUI_QCL()
		
	def closeSerial(self):
		print('closing serial port')
		self.qcl.disconnect()
		self.disableUI_QCL()
		self.updateSerialList()
		
	def powerComb1(self):
		comb = 1
		
		actual_state = self.comb_power[comb-1]
		new_state = int(not(actual_state))
		self.qcl.powerComb(comb, new_state)
		self.comb_power[comb-1] = new_state
		#self.updateUI()

		if new_state == 0:
			#QCL is not off, turn button red and change text to 'Turn power ON'
			self.pushButton_Comb1_power.setText('Turn power ON')
			self.pushButton_Comb1_power.setStyleSheet('background-color: red')
		else:
			#QCL is not on, turn button green and change text to 'Turn power OFF'
			self.pushButton_Comb1_power.setText('Turn power OFF')
			self.pushButton_Comb1_power.setStyleSheet('background-color: green')

		
		
	def enableComb1(self):
		comb = 1

		actual_state = self.comb_enable[comb-1]
		new_state = int(not(actual_state))
		self.qcl.enableComb(comb, int(not(actual_state)))
		self.comb_enable[comb-1] = new_state
		#self.updateUI()

		if new_state == 0:
			#QCL is not off, turn button red and change text to 'Enable output'
			self.pushButton_Comb1_enable.setText('Enable output')
			self.pushButton_Comb1_enable.setStyleSheet('background-color: red')
		else:
			#QCL is not on, turn button green and change text to 'Disable output'
			self.pushButton_Comb1_enable.setText('Disable output')
			self.pushButton_Comb1_enable.setStyleSheet('background-color: green')
	
	def powerComb2(self):
		comb = 2
		
		actual_state = self.comb_power[comb-1]
		new_state = int(not(actual_state))
		self.qcl.powerComb(comb, new_state)
		self.comb_power[comb-1] = new_state
		#self.updateUI()

		if new_state == 0:
			#QCL is not off, turn button red and change text to 'Turn power ON'
			self.pushButton_Comb2_power.setText('Turn power ON')
			self.pushButton_Comb2_power.setStyleSheet('background-color: red')
		else:
			#QCL is not on, turn button green and change text to 'Turn power OFF'
			self.pushButton_Comb2_power.setText('Turn power OFF')
			self.pushButton_Comb2_power.setStyleSheet('background-color: green')


	def enableComb2(self):
		comb = 2

		actual_state = self.comb_enable[comb-1]
		new_state = int(not(actual_state))
		self.qcl.enableComb(comb, int(not(actual_state)))
		self.comb_enable[comb-1] = new_state
		#self.updateUI()

		if new_state == 0:
			#QCL is not off, turn button red and change text to 'Enable output'
			self.pushButton_Comb2_enable.setText('Enable output')
			self.pushButton_Comb2_enable.setStyleSheet('background-color: red')
		else:
			#QCL is not on, turn button green and change text to 'Disable output'
			self.pushButton_Comb2_enable.setText('Disable output')
			self.pushButton_Comb2_enable.setStyleSheet('background-color: green')

	
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
