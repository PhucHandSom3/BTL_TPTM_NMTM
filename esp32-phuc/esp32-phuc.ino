#include <WiFi.h>
#include <HTTPClient.h>

// Cấu hình Wi-Fi
const char* ssid = "test123";
const char* password = "12345678";

// Flask server URL
const char* serverUrl = "http://192.168.138.158:5000/data";

void setup() {
  Serial.begin(115200); // Debug qua USB
  delay(1000); // Đợi ổn định UART

  Serial2.begin(9600, SERIAL_8N1, 16, 17); // RX = GPIO16, TX không dùng
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ WiFi connected!");
}

void loop() {
  if (Serial2.available()) {
    String data = Serial2.readStringUntil('\n');
    data.trim();

    if (data.startsWith("PH:") && data.indexOf("TURB:") != -1) {
      Serial.println("📥 Nhận từ Uno: " + data);

      if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverUrl);
        http.addHeader("Content-Type", "application/json");

        String jsonData = "{\"sensor_data\": \"" + data + "\"}";
        int httpCode = http.POST(jsonData);

        Serial.print("📡 Gửi đến web: ");
        Serial.println(httpCode);

        http.end();
      }
    } else {
      Serial.println("⚠️ Dữ liệu không hợp lệ: " + data);
    }
  }

  delay(100); // Tránh overload
}
