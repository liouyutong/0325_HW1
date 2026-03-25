#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 Sensor Test...");
  dht.begin();
}

void loop() {
  delay(2000);

  // 讀取濕度、溫度
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // 讀取是否失敗
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("DATA:溫度：");
  Serial.print(t);
  Serial.print(",濕度：");
  Serial.println(h);
}