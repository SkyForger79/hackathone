const int trigPin = 27;
const int echoPin = 14;
long distance;
// Определение времени задержки
long getEchoTiming() {
  digitalWrite(trigPin, HIGH); // генерируем 10 мкс импульс запуска
  delayMicroseconds(10);  
  digitalWrite(trigPin, LOW);
  // определение на пине echoPin длительности уровня HIGH, мкс:
  long duration = pulseIn(echoPin, HIGH); 
  return duration;
  }
// Определение дистанции до объекта в см

long getDistance() {
  long distacne_cm = getEchoTiming() * 1.7 * 0.01;
  return distacne_cm;
}

long Sonar()
{ 
  distance = getDistance(); // получаем дистанцию с датчика
  return(distance);
}
void Sonar_print() 
{ 
  distance = getDistance(); // получаем дистанцию с датчика
  Serial.print("Distance:   ");
  Serial.println(distance); // выводим в последовательный порт
}
