int motorPin11 = 3;
int motorPin21 = 5;
int motorPin31 = 9;
int motorPin41 = 10;
float stepspdegree = 900.0/360.0;

int delayTime = 5;
int i=0; 


//Definir graus a rodar
int graus;

String inputString = "";
bool stringComplete = false;
String message = "";


int steps=100;

void setup() {
  pinMode(motorPin11, OUTPUT);
  pinMode(motorPin21, OUTPUT);
  pinMode(motorPin31, OUTPUT);
  pinMode(motorPin41, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(1000);
}




void loop() {

while(Serial.available()==0){
}  
  serialEvent();
  
  
  Serial.println(inputString);
  
  graus = inputString.toInt();

  
  steps = int(graus * stepspdegree);
  
  i = 0;
  

  
while(i<steps){
  
  cycle();
  i++;
  //Serial.print(millis());
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

/*
void serialEvent(){
  inputString="";
  while(Serial.available()){
    char inChar = (char)Serial.read();

    inputString += inChar;

    }
Serial.flush();
}
*/

void serialEvent(){
  inputString = "";
  while(Serial.available()){
    inputString=Serial.readString();

    }
Serial.flush();
}
