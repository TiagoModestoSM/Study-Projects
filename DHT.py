import serial

# Configure a porta serial e a taxa de transmissão
ser = serial.Serial('COM5', 9600, timeout=1)  # Altere 'COM3' para a porta do seu Arduino
print('Sensor de temperatura e humidade')
def process_data(data):
    try:
        parts = data.split('\t')
        umidade = parts[0].split(':')[1].strip().replace('%', '')
        temperatura = parts[1].split(':')[1].strip().replace(' °C', '')
        heat_index_f = parts[2].split(':')[1].strip().replace(' °F', '')
        heat_index_c = parts[3].split(':')[1].strip().replace(' °C', '')
        return umidade, temperatura, heat_index_f, heat_index_c
    except (IndexError, ValueError):
        return None, None, None, None

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if "Umidade:" in line:
                print(line)
                print('--------------------------------------------------------------------------------------------')
                umidade, temperatura, heat_index_f, heat_index_c = process_data(line)
                

                    
except KeyboardInterrupt:
    print("Programa interrompido.")
finally:
    ser.close()  # Fecha a conexão serial
