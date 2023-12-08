import serial
import os
import psycopg2
from psycopg2 import sql
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
db_config = {
    'host': os.getenv('DB_HOST'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

# Configurações da porta serial
serial_port = 'COM4'  # Substitua pelo seu valor específico
baud_rate = 9600

# Conectar ao banco de dados PostgreSQL

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()


# Configurar a conexão serial
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Ler dados da porta serial
        serial_data = ser.readline().decode('utf-8').strip()

        # Aqui você pode processar os dados conforme necessário
        # Exemplo: Dividir os dados e armazenar em variáveis
        data_parts = serial_data.split(',')
        valor1 = float(data_parts[0])*(4.47/1024)
        print(valor1)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Inserir dados no banco de dados
        insert_query = sql.SQL("INSERT INTO tabela_dados (timestamp_col, tensao) VALUES ({}, {})").format(
            sql.Literal(timestamp),
            sql.Literal(valor1),
        )
        cursor.execute(insert_query)
        conn.commit()

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
finally:
    # Fechar conexões ao encerrar o programa
    ser.close()
    cursor.close()
    conn.close()