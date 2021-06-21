#include <Servo.h>
Servo left;
Servo right;

void setup()
{
Serial.begin(9600);
pinMode(8, OUTPUT);
left.attach(9);
right.attach(10);
}

String input;
int ctrl;

void loop()
{
    if (Serial.available())
    {
        input = Serial.readString();
        ctrl = input.toInt();
        left.write(ctrl);
        right.write(ctrl);
    }
}