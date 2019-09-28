#include <DHT.h>
#define DHTPIN 13//был 25    
float Humidity;
float temperature;
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);
void temperatyre() 
 { 
  Humidity = dht.readHumidity();
  temperature = dht.readTemperature();   
  if (isnan(Humidity) || isnan(temperature)) {
    Serial.println("Error while reading the sensor");
    return;
  }
  Serial.print("Humidity: ");
  Serial.println(Humidity);
  Serial.println("-----------------------------------------------------------");
  Serial.print("temperature: ");
  Serial.println(temperature);

}
