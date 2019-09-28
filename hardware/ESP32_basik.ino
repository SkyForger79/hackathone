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

*/    //в случае встряски посылаем сообщение серверу
    // посылаем HTTP-запрос:
    Json= "%7B%22Light%22:%Light%20%22:%"+ String(Svet) +", %20%22microphoneValue:%22%" + String(microphoneValue) + ",%20%22Sonar:%22%" + String(distance) + ",%20%22Humidity:%22%" + String(H) + ",%20%22temperature:%22%" + String(T) + "%7D";
    Serial.println(Json);
    http.begin("http://192.168.0.102:9999/v1/set_stat?Light=" + String(Svet) + "&microphoneValue=" + String(microphoneValue) + "&Sonar=" + String(distance) + "&Humidity=" + String(H) + "&temperature=" + String(T)); //передача сообщения на сервер
    Serial.println("--------------------------------------------------------------------------");
    Serial.println("http://192.168.0.102:9999/v1/set_stat/" + Json);
    Serial.println("--------------------------------------------------------------------------");
    int httpcode = http.GET();
    Serial.print("Error code: ");
    Serial.println(httpcode);
    http.end();
    
    delay(500);

}
