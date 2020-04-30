int motorPins[] = {8, 9, 10, 11};
int idx = 0;
int count2 = 0;
int delayTime = 100;
int val = 0;
int k = 0;
byte j= 0;

//COM Variables
char data = "";
String message = "";
int number;

void setup() {
  for (idx = 0; idx < 4; idx++) {
    pinMode(motorPins[idx], OUTPUT); //Definição de todos os pinos para o motor como OUTPUT
  }
  Serial.begin(115200);
}



void moveRequested(int steps) {//Function to move desired steps(moves 30 degrees/step)

if(steps>0){  
  for(int t= 0; t<steps; t++){
  j=0b00010000;
  
  //count2 = 16; //Definir binário 0b00001111
  while(j>1){
  j>>=1; //Definir binário 0b00000111
 
  for (idx = 3; idx >= 0; idx--) {
    digitalWrite(motorPins[idx], j>>idx&0x01);
  }
  delay(delayTime);
 }
 }
}
else if(steps<0){
for(int t= 0; t>steps; t--){
  j=0b00010000;
  
  //count2 = 16; //Definir binário 0b00001111
  while(j>1){
  j>>=1; //Definir binário 0b00000111
 
  for (idx = 3; idx >= 0; idx--) {
    digitalWrite(motorPins[3 - idx], j>>idx&0x01);
  }
  delay(delayTime);
 }
 }
}
  }



void loop() {
while (Serial.available() == 0) {} //Locks program while there is no comunication

if(Serial.available() > 0) {
    message="";
    data = Serial.read();
    char str[2];   
    str[0] = data;
    str[1] = '\0';
       

message = str;

number = message.toInt();


moveRequested(number);
  
 
}

}
