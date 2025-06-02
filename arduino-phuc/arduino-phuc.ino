// UNO gửi dữ liệu cảm biến qua UART
const int PH_PIN = A0;
const int TURBIDITY_PIN = A1;

void setup() {
  Serial.begin(9600); // Gửi dữ liệu sang ESP32
}

void loop() {
  int phValue = analogRead(PH_PIN);
  int turbidityValue = analogRead(TURBIDITY_PIN);

  Serial.print("PH:");
  Serial.print(phValue);
  Serial.print(",TURB:");
  Serial.println(turbidityValue); // Gửi định dạng rõ ràng

  delay(2000); // Gửi mỗi 2 giây
}
