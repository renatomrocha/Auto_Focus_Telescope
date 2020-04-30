int motorPin11 = 3;
int motorPin21 = 4;
int motorPin31 = 5;
int motorPin41 = 6;
int motorPin12 = 7;
int motorPin22 = 8;
int motorPin32 = 9;
int motorPin42 = 10;


int delayTime = 100;
int i=0;


void setup() {
  pinMode(motorPin11, OUTPUT);
  pinMode(motorPin21, OUTPUT);
  pinMode(motorPin31, OUTPUT);
  pinMode(motorPin41, OUTPUT);
 pinMode(motorPin12, OUTPUT);
  pinMode(motorPin22, OUTPUT);
  pinMode(motorPin32, OUTPUT);
  pinMode(motorPin42, OUTPUT);

}




void loop() {


while(i<12){
  
  cycle();
  i++;
  }

  
}

void cycle() {
 digitalWrite(motorPin11, HIGH);
 digitalWrite(motorPin12, LOW);
  
  digitalWrite(motorPin21, LOW);
  digitalWrite(motorPin22, HIGH);
 
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin32, HIGH);
 
  digitalWrite(motorPin41, LOW);
  digitalWrite(motorPin42, HIGH);
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin12, HIGH);
 
  digitalWrite(motorPin21, HIGH);
  digitalWrite(motorPin22, LOW);
 
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin32, HIGH);
 
  digitalWrite(motorPin41, LOW);
  digitalWrite(motorPin42, HIGH);
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin12, HIGH);
 
  digitalWrite(motorPin21, LOW);
  digitalWrite(motorPin22, HIGH);
 
  digitalWrite(motorPin31, HIGH);
  digitalWrite(motorPin32, LOW);
 
  digitalWrite(motorPin41, LOW);
  digitalWrite(motorPin42, HIGH);
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  
  digitalWrite(motorPin21, LOW);
  
  digitalWrite(motorPin31, LOW);
  
  digitalWrite(motorPin41, HIGH);
  
  delay(delayTime); 
}
