#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

unsigned long lastTime = 0;
unsigned long gyroDelay = 10;

unsigned long lastTimesensores = 0;
unsigned long sensores = 500;

Adafruit_MPU6050 mpu;
sensors_event_t a, g, temp;

float gyroZ;

float gyroZerror = 0.01;

const int s1 = 2;
const int s2 = 3;
const int s3 = 4;
const int s4 = 5;
const int s5 = 6;

const int GIRO_D = 7;
const int GIRO_I = 8;

int stes1;
int stes2;
int stes3;
int stes4;
int stes5;

void initMPU()
{
  if(!mpu.begin())
  {
    Serial.println("Failed to find MPU6050 chip");
    while(1)
    {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
}

float getGyroReadings()
{
  mpu.getEvent(&a,&g,&temp);

  float gyroZ_temp = g.gyro.z;
  if(abs(gyroZ_temp) > gyroZerror)
  {
    gyroZ += gyroZ_temp/90.00;
  }
  
  float readingZ = gyroZ;

  if(readingZ >= 1.21 || readingZ <= -1.21)
  {
    gyroZ=0.00;
  }
  return readingZ;
}

void setup()
{
  pinMode(s1,INPUT_PULLUP);
  pinMode(s2,INPUT_PULLUP);
  pinMode(s3,INPUT_PULLUP);
  pinMode(s4,INPUT_PULLUP);
  pinMode(s5,INPUT_PULLUP);

  pinMode(GIRO_D,OUTPUT);
  pinMode(GIRO_I,OUTPUT);

  digitalWrite(GIRO_D,LOW);
  digitalWrite(GIRO_I,LOW);

  Serial.begin(9600);
  initMPU();
}

void lectura()
{
  stes1 = digitalRead(s1);
  stes2 = digitalRead(s2);
  stes3 = digitalRead(s3);
  stes4 = digitalRead(s4);
  stes5 = digitalRead(s5);

  stes1 = !stes1;
  stes2 = !stes2;
  stes3 = !stes3;
  stes4 = !stes4;
  stes5 = !stes5;
  
    if((!stes1 && !stes2 && stes3) || (!stes2 &&  stes3 && stes5) || (!stes1 && stes2 && stes5) || (!stes1 && stes4) || (stes4 && stes5))
    {
      digitalWrite(GIRO_I,HIGH);
      digitalWrite(GIRO_D,LOW); 
    }
    else if((stes2 && !stes4 && !stes5)||(stes1 && stes4 && !stes5)||(stes1 && stes3 && !stes5)||(stes1 && stes2 && !stes4))
    {
      digitalWrite(GIRO_D,HIGH);
      digitalWrite(GIRO_I,LOW);   
    }
    else
    {
      digitalWrite(GIRO_I,LOW);
      digitalWrite(GIRO_D,LOW);
    }
    delay(500);
}

void showit()
{
  if((millis()-lastTime)>gyroDelay)
  {
    Serial.println(getGyroReadings());
    lastTime = millis();
  }
}

void loop()
{
  showit();
  lectura();
}
