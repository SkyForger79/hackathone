#define sensorD0 33//был 13 входной пин для выхода D0 с микрофона 
int microphoneValue = 0;// переменная для значения 
 
int Screem ()
{
  microphoneValue = analogRead(sensorD0); // чтение значения с микрофона
  return(microphoneValue);

}
void Screem_print()
{
  microphoneValue = analogRead(sensorD0); // чтение значения с микрофона
  Serial.print("Noize:  ");
  Serial.println (microphoneValue, DEC); // вывод значения в монитор порта
}
