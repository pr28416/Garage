void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  // for (int i = 0; i < 10; i++) {
  //   for (int j = 0; j <= i; j++) {
  //     digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  //     digitalWrite(11, HIGH);   // turn the LED on (HIGH is the voltage level)
  //     delay(100);                       // wait for a second
  //     digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  //     digitalWrite(11, LOW);    // turn the LED off by making the voltage LOW
  //     delay(100);                       // wait for a second   
  //   }
  //   delay(500);
  // }
  int pin = rand() % 3 + 10;
  digitalWrite(pin, HIGH);
  delay(100);
  digitalWrite(pin, LOW);
  delay(100);

  return;
}