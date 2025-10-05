#include <Servo.h>
Servo duoji;

void setup() {
  // put your setup code here, to run once:
  duoji.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  duoji.write(0);
  delay(1000);
  duoji.write(30);
  delay(1000);
  duoji.write(45);
  delay(1000);
  duoji.write(90);
  delay(1000);
  duoji.write(135 ;
  delay(1000);
}
