#include <Servo.h>
Servo left;
Servo right;

void setup()
{
Serial.begin(9600);
left.attach(9);
right.attach(10);
left.write(0);
right.write(0);
Serial.setTimeout(50);
}

int ctrl = 0;
String input;
char next;


void loop()

{
    if(Serial.available() > 0){
        input = Serial.readString();
        ctrl = input.toInt();
        Serial.println(ctrl);
     }
     left.write(ctrl+127);
     right.write(ctrl+127);
}
















