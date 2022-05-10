const int LED = 2;

void setup()
{
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
  delay(100);
  Serial.println("Hi Pico");
  digitalWrite(LED,LOW);
}

void loop()
{
  float numero = 1.30;
  digitalWrite(LED,HIGH);
  Serial.println(numero);
  delay(500);
  digitalWrite(LED,LOW);
  delay(200);
}
