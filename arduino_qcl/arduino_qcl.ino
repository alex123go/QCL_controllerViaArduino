/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

String stringTemp;
String stringIn;
char c;

int pin0 = 10;
int pin1 = 11;
int pin2 = 12;
int pin3 = 13;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);
  pinMode(pin0,OUTPUT);
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  while(Serial.available() > 0) 
  {
    c = Serial.read();
    if (c == '\n') 
    {
      stringIn = stringTemp;
      stringTemp = "";
      break;
    }
    stringTemp += c;
  }
if (stringIn == "A0?")
  {
   Serial.println(analogRead(A0));
  }
else if (stringIn == "A1?")
  {
    Serial.println(analogRead(A1)); 
  }
else if (stringIn == "A2?")
  {
    Serial.println(analogRead(A2));
  }
else if (stringIn == "A3?")
  {
    Serial.println(analogRead(A3));
  }
else if (stringIn == "A4?")
  {
    Serial.println(analogRead(A4));
  }
else if (stringIn == "A5?")
  {
    Serial.println(analogRead(A5));
  }
else if (stringIn == "A6?")
  {
    Serial.println(analogRead(A6));
  }
else if (stringIn == "A7?")
  {
    Serial.println(analogRead(A7));
  }
else if (stringIn == "A8?")
  {
    Serial.println(analogRead(A8));
  }
else if (stringIn == "A9?")
  {
    Serial.println(analogRead(A9));
  }
else if (stringIn == "A10?")
  {
    Serial.println(analogRead(A10));
  }

  
else if (stringIn == "Power1:0")
  {
    digitalWrite(pin0,0);
  }
else if (stringIn == "Power1:1")
  {
    digitalWrite(pin0,1);
  }
else if (stringIn == "Enable1:0")
  {
    digitalWrite(pin1,0);
  }
else if (stringIn == "Enable1:1")
  {
    digitalWrite(pin1,1);
  }
else if (stringIn == "Power2:0")
  {
    digitalWrite(pin2,0);
  }
else if (stringIn == "Power2:1")
  {
    digitalWrite(pin2,1);
  }
else if (stringIn == "Enable2:0")
  {
    digitalWrite(pin3,0);
  }
else if (stringIn == "Enable2:1")
  {
    digitalWrite(pin3,1);
  }
  
else if (stringIn == "PowerAll:0")
  {
    digitalWrite(pin0,0);
    digitalWrite(pin2,0);
  }
  else if (stringIn == "PowerAll:1")
  {
    digitalWrite(pin0,1);
    digitalWrite(pin2,1);
  }
else if (stringIn == "EnableAll:0")
  {
    digitalWrite(pin1,0);
    digitalWrite(pin3,0);
  }
  else if (stringIn == "EnableAll:1")
  {
    digitalWrite(pin1,1);
    digitalWrite(pin3,1);
  }

  stringIn = "";
  delay(1);        // delay in between reads for stability
}
