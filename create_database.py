import os
import psycopg2
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Conectar ao PostgreSQL

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

conn = psycopg2.connect(**db_config)
conn.autocommit =True

# Criar um cursor
cursor = conn.cursor()

try:
    with open("create_database.sql", "r") as f:
        cursor.execute(f.read())

except Exception as e:
    print(f"Erro ao criar ou verificar a base de dados: {e}")

cursor.close()
conn.close()


