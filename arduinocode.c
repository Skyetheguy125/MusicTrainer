// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
int numSamples = 0;
unsigned long startTime = 0;
while (numSamples < 1000){
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(0.304);  
  numSamples++;// delay in between reads for stability
}

unsigned long endTime = millis();
 Serial.println(endTime - startTime);
}