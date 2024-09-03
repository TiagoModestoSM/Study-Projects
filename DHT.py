#|Autor: Tiago Modesto (Labigó)                           |
#|Data:04/06/2024                                         |
#|Teste de código do Sensor DHT11 de Umidade e Temperatura|
#|Implementa o Serial do arduino no python                |


import serial
from datetime import datetime

# Configure a porta serial e a taxa de transmissão
ser = serial.Serial('COM5', 9600)  # Altere 'COM3' para a porta do seu Arduino
ser.timeout = 1  # Timeout para leitura (em segundos)

try:
    while True:
        # Obter a hora atual
        now = datetime.now()
        # Formatando a hora
        hora_formatada = now.strftime('%Y-%m-%d %H:%M:%S')
        if ser.in_waiting > 0:  # Verifica se há dados disponíveis
            line = ser.readline().decode('utf-8').strip()
            
            print(line)
            print("Hora atual:", hora_formatada)
            # Extrair dados usando divisão e limpeza
            parts = line.split('\t')
            if len(parts) == 4:
                umidade = parts[0].split(':')[1].strip().replace('%', '')
                temperatura = parts[1].split(':')[1].strip().replace(' °C', '')
                heat_index_f = parts[2].split(':')[1].strip().replace(' °F', '')
                heat_index_c = parts[3].split(':')[1].strip().replace(' °C', '')

                # Exibe os dados extraídos
                #print(f"Temperatura: {temperatura}°C")
                #print(f"Heat Index (F): {heat_index_f}°F")
                #print(f"Heat Index (C): {heat_index_c}°C")
                
except KeyboardInterrupt:
    print("Programa interrompido.")
finally:
    ser.close()  # Fecha a conexão serial
