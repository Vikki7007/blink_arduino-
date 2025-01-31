/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
*/

// the setup function runs once when you press reset or power the board
#define LED_PIN 4  // Flash LED on ESP32-CAM is connected to GPIO 4
#define LED_PIN 13
void setup() {
  pinMode(13, OUTPUT); // Set LED pin as output
}

void loop() {
  digitalWrite(13, HIGH);  // Turn the LED on
  delay(250);                  // Wait for a second
  digitalWrite(13, LOW);   // Turn the LED off
  delay(250);                  // Wait for a second
  
}


