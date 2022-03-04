#include <Arduino.h>
//test
const int Slider = 6;
const int Inputs[Slider]= {A0, A1, A2, A3, A4, A5};

int Values[Slider];

void setup() {
  // init all defined pins for sliders 
  for ( int i = 0; i < Slider; i++){
    pinMode(Inputs[i], INPUT);
  }
  Serial.begin(9600);
}

void readValues(){
  for (int i = 0; i < Slider; i++){
    Values[i] = analogRead(Inputs[i]);
  }
}

void sendValues(){
  String send = "{ ";
  for (int i = 0; i < Slider; i++){
    if (i == Slider-1){
      send = send + " \"Slider"+i+"\": "+Values[i]+ "";
    }else{
      send = send + " \"Slider"+i+"\": "+Values[i]+ ",";
    }
  }
  send = send + " }";
  Serial.println(send);
}

void loop() {
  readValues();
  sendValues();
}

