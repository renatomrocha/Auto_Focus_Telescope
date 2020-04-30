int motorPin11 = 3;
int motorPin21 = 5;
int motorPin31 = 9;
int motorPin41 = 10;


int delayTime = 5;
int i=0;


void setup() {
  pinMode(motorPin11, OUTPUT);
  pinMode(motorPin21, OUTPUT);
  pinMode(motorPin31, OUTPUT);
  pinMode(motorPin41, OUTPUT);


}




void loop() {


while(i<900){
  
  cycle();
  i++;
  }

  
}

void cycle() {
 digitalWrite(motorPin11, HIGH);
 digitalWrite(motorPin21, LOW);
  
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41,LOW);
 
  
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin21, HIGH);
 
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41, LOW);
 
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin21, LOW);
 
  digitalWrite(motorPin31, HIGH);
  digitalWrite(motorPin41, LOW);
 
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin21, LOW);
  
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41, HIGH);

  delay(delayTime); 
}
