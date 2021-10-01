# QCL_controllerViaArduino
Control a QCL driver (QCL500 OEM or QCL 1500 OEM) via the GPIO pins of an arduino

## Python
The python software runs a PyQt5 graphical user interface (GUI) and send serial commands according the the button pressed.
Note : Due to the reset configuration of the Arduino, all outputs are reseted when a new serial connection is made. Therefore, the QCL's outputs are all turned off when you reconnect to the arduino.

To run the python software, either
```
python QCL_GUI.py
```
or run the .exe file.

## Arduino
The arduino software allows controlling a QCL driver via a python user interface.
It controls 4 output pins according to the serial messages received.

## Create executable file w/ WinPython
In the WinPython-x.x folder, run "WinPython Command Prompt.exe"
```
pip install pyinstaller
cd "here"
pyinstaller --onefile -w QCL_GUI.py
copy QCL_GUI.ui dist\
```

The last line is to make sure the .ui file is kept with the .exe file.
You need to share both file for the software to work
