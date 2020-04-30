int motorPin11 = 3;
int motorPin21 = 5;
int motorPin31 = 9;
int motorPin41 = 10;
float stepspdegree = 900.0/360.0;

bool zeroing = false; 

int delayTime = 5;
int i=0; 

byte iPin = 2;

//Definir graus a rodar
int graus;

String inputString = "";
bool stringComplete = false;
String message = "";


int steps=100;

bool turnRight = false;
bool turnLeft = false;
bool Stop = false;


int stepsExecutados=0;



void setup() {
  pinMode(motorPin11, OUTPUT);
  pinMode(motorPin21, OUTPUT);
  pinMode(motorPin31, OUTPUT);
  pinMode(motorPin41, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(1000);
  attachInterrupt(digitalPinToInterrupt(iPin),service,FALLING); // Falling edge at iPin
}




void loop() {
Serial.println("Init");
while(Serial.available()==0){
  if(turnRight==true){
    continuousRight();
}
  else if(turnLeft==true){
    continuousLeft();
}
  
}  
  serialEvent();
  
  Serial.println(inputString);

if(inputString.equals("Zero\n")){
  Serial.println("Vou zerar");
  zeroing = true;
  zero();
}
else if(inputString.equals("Right\n")){
  turnRight = true;
  continuousRight();
  Serial.println("Vou virar para a direita");
}
else if(inputString.equals("Left\n")){
  turnLeft = true;
  continuousLeft();
  Serial.println("Vou virar para a esquerda");
}  
else if(inputString.equals("Stop\n")){
  turnLeft=false;
  turnRight=false;
  Serial.println("Vou parar");
  Serial.print("Rodei: ");
  Serial.println(stepsExecutados);
  stepsExecutados = 0;
}  
else{
  turnDegrees();
}  
 
}

void continuousRight(){
  Serial.println("-->");
  stepsExecutados++;
}


void continuousLeft(){
  Serial.println("<--"); 
  stepsExecutados++;
}


void turnDegrees(){
  
  graus = inputString.toInt();
  Serial.print("Vou rodar em graus: " );
  Serial.println(graus);
  steps = int(graus * stepspdegree);
  
  i = 0;
  

  
while(i!=steps){
if(steps>0){  
  cycle();
  i++;
}
  //Serial.print(millis());
else if (steps<0){
  rev_cycle();
  i--;
  
  }  
  
  }
  }


void service(){
  Serial.println("Stop");
  zeroing = false;
}

void zero(){
  while(zeroing){
  rev_cycle();  
  Serial.println(zeroing);
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


void rev_cycle() {
 digitalWrite(motorPin11, LOW);
 digitalWrite(motorPin21, LOW);
  
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41,HIGH);
 
  
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin21, LOW);
 
  digitalWrite(motorPin31, HIGH);
  digitalWrite(motorPin41, LOW);
 
 
  delay(delayTime);
  
  digitalWrite(motorPin11, LOW);
  digitalWrite(motorPin21, HIGH);
 
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41, LOW);
 
  delay(delayTime);
  
  digitalWrite(motorPin11, HIGH);
  digitalWrite(motorPin21, LOW);
  
  digitalWrite(motorPin31, LOW);
  digitalWrite(motorPin41, LOW);

  delay(delayTime); 
}


void serialEvent(){
  inputString = "";
  while(Serial.available()){
    inputString=Serial.readString();

    }
Serial.flush();
}
