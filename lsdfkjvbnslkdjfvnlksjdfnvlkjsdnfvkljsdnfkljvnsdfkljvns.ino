int trigPin = 4;
int echoPin = 5;
unsigned long duration = 0;
 
void setup()
{
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop() 
{
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  Serial.println(duration);

}
