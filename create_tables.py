import os
import psycopg2
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Conectar ao PostgreSQL

db_config = {
    'host': os.getenv('DB_HOST'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

conn = psycopg2.connect(**db_config)

# Criar um cursor
cursor = conn.cursor()

try:
    with open("create_tables.sql", "r") as f:
        print(cursor.execute(f.read()))

except Exception as e:
    print(f"Erro ao criar ou verificar as tables: {e}")
cursor.close()
print(conn.commit())
conn.close()


