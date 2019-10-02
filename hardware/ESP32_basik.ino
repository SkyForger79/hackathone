#include <SPI.h>
#include <WiFi.h>
#include "sonar.h"
#include "temperatyre.h"
#include "microphone.h"
#include <HTTPClient.h>
#define SensorPin 32

const char* ssid     = "EL123";
const char* password = "EL27072019";
const uint16_t port = 9999;//9999;

int status = WL_IDLE_STATUS;
const char * host = "192.168.0.102";
WiFiClient client;
HTTPClient http;
int L,Mi;
float H,T;
long S;
int Svet = 0;
String Json ;
//Фоторезистор
int Light()
{
   // Получаем данные с модуля
    Svet = analogRead(SensorPin);
    return(Svet);
}
void Light_print()
{
   // Получаем данные с модуля
    Svet = analogRead(SensorPin);
    // Выводим значение полученное с модуля
    Serial.print("Light:    ");
    Serial.println(Svet, DEC);
    // Задержка
    delay(200);
}

void setup()  {
  pinMode(26, OUTPUT);//красный светик
  digitalWrite(26, LOW);
  pinMode(trigPin, OUTPUT); // триггер - выходной пин
  pinMode(echoPin, INPUT); // эхо - входной
  digitalWrite(trigPin, LOW);
  Serial.begin(115200); // инициализация послед. порта
  dht.begin();
  pinMode (sensorD0, INPUT);
  Serial.println("KY-015 test - temperature and humidity-test:");

   WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(26, HIGH);
    delay(100);
    digitalWrite(26, LOW);
    delay(100);
    Serial.print(".");
  }
  Serial.println("WiFi connected ");
 if (!client.connect(host, port)) {
Serial.println("Connection to host failed");
digitalWrite(26, HIGH);
delay(1000);
digitalWrite(26, LOW);
delay(300);
digitalWrite(26, HIGH);
delay(1000);
digitalWrite(26, LOW); 
 return;
    }
    
  Serial.print("Server connected with IP: ");
  Serial.println(WiFi.localIP());
}

void loop()  
{
  S = Sonar();
  T = dht.readTemperature();
  H = dht.readHumidity();
  L = Light();
  Mi = Screem();

    // посылаем HTTP-запрос:
    Json= "{Light: "+ String(Svet) +", microphoneValue: " + String(microphoneValue) + ",Sonar: " + String(distance) + ",Humidity: " + String(H) + ", temperature: " + String(T) + "}";
    Serial.println(Json);
    if(S<=10 || T>=26 || H>=20 || L>=1700)
    {
      http.begin("http://192.168.0.102:9999/v1/set_stat?Light=" + String(Svet) + "&microphoneValue=" + String(microphoneValue) + "&Sonar=" + String(distance) + "&Humidity=" + String(H) + "&temperature=" + String(T)); //передача сообщения на сервер
      int httpcode = http.GET();
      Serial.print("Error code: ");
      Serial.println(httpcode);
      http.end();
    }
      Serial.println("--------------------------------------------------------------------------");
      Serial.println("http://192.168.0.102:9999/v1/set_stat/" + Json);
      Serial.println("--------------------------------------------------------------------------");

    delay(100);

}
