-- create_tables.sql
CREATE TABLE tabela_dados (
    id SERIAL PRIMARY KEY,
    timestamp_col TIMESTAMP,
    tensao FLOAT
);