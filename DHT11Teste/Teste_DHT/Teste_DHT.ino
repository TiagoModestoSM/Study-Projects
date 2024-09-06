/*
|Autor: Tiago Modesto (Labigó)                           |
|Data:04/06/2024                                         |
|Teste de código do Sensor DHT11 de Umidade e Temperatura|
*/

// Definição de Bibliotecas
#include <DHT.h>
#include <DHT_U.h>

// Definição dos pinos
#define PinledR 8 // LED vermelho
#define PinledG 7 // LED verde
#define DHTPIN 3 // Pino de sinal do DHT11
#define DHTTYPE DHT11 // Modelo do sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); // Inicia a comunicação serial
  Serial.println("SENSOR DE TEMPERATURA E HUMIDADE");

  
  pinMode(PinledR, OUTPUT);
  pinMode(PinledG, OUTPUT);
  dht.begin();
  
  // Inicialmente, apaga ambos os LEDs
  digitalWrite(PinledR, LOW);
  digitalWrite(PinledG, LOW);

}

void loop() {
  // Primeiro, tenta fazer a leitura do sensor
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // Celsius é o padrão
  float f = dht.readTemperature(true); // Lê em Fahrenheit

  if (isnan(h) || isnan(t) || isnan(f)) {
    // Se falhar a leitura, acende o LED vermelho e aguarda 2 segundos
    digitalWrite(PinledR, HIGH);
    digitalWrite(PinledG, LOW); // Garante que o LED verde esteja apagado
    Serial.println("------------------------------------------------------------------------------------------------------------");
    Serial.println("Falha na leitura do sensor DHT");
    Serial.println("------------------------------------------------------------------------------------------------------------");
    delay(2000); // Espera 2 segundos antes de tentar a leitura novamente
    digitalWrite(PinledR, LOW); // Desliga o LED vermelho
    return; // Sai do loop para evitar leituras adicionais com falha
  }
  
  // Se a leitura for bem-sucedida, acende o LED verde para indicar uma nova leitura
  digitalWrite(PinledR, LOW); // Garante que o LED vermelho esteja apagado
  digitalWrite(PinledG, HIGH); // Acende o LED verde
  delay(200); // O LED verde pisca por 200 ms
  digitalWrite(PinledG, LOW); // Apaga o LED verde

  // Calcula o índice de calor
  float hif = dht.computeHeatIndex(f, h); // Temperatura em Fahrenheit
  float hic = dht.computeHeatIndex(t, h, false); // Temperatura em Celsius

  // Mostra os valores no Serial Monitor com formatação
    Serial.println("------------------------------------------------------------------------------------------------------------");
  Serial.print("| Umidade:  ");
  Serial.print(h, 1); // Imprime com uma casa decimal
  Serial.print(" %\t|");
  Serial.print(" Temperatura:  ");
  Serial.print(t, 1); // Imprime com uma casa decimal
  Serial.print(" °C\t |");
  Serial.print(" Heat Index (F):  ");
  Serial.print(hif, 1); // Imprime com uma casa decimal
  Serial.print(" °F\t |");
  Serial.print(" Heat Index (C):  ");
  Serial.print(hic, 1); // Imprime com uma casa decimal
  Serial.println(" °C |");


  // Aguarda 2 segundos antes da próxima leitura
  delay(2000);
}
