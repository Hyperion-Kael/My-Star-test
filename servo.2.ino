#include<Servo.h>;
Servo duoji;

void setup() {
  // put your setup code here, to run once:
  duoji.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  int num[5]={0,30,45,90,135};
  int i;
  for(i=0;i<5;i++)
  {
    duoji.write(num[i]);
    delay(1000);
  } 
}
