#include <Servo.h>
Servo left;
Servo right;

void setup()
{
Serial.begin(9600);
pinMode(7, INPUT_PULLUP);
pinMode(6, INPUT_PULLUP);
left.attach(9);
right.attach(10);
left.write(127);
right.write(127);

}

int rb;
int lb;

void loop()
{
lb = not digitalRead(7);
rb = not digitalRead(6);
Serial.print(lb);
Serial.println(rb);

  if(lb){
     left.write(77);
     right.write(77);
  }
  if(rb){
     left.write(177);
     right.write(177);
  }
  if(not rb and not lb){
     left.write(127);
     right.write(127);    
  }
}