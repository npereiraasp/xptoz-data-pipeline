# Databricks notebook source
import os
import psycopg2
from faker import Faker

DB_CONFIG = {
    "host": "postgres",
    "user": "airflow",
    "password": "airflow",
    "port": "5432",
    "dbname": "airflow"
}

def conectar_banco():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def criar_tabela():
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS public.users_info (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                idade INT,
                cidade VARCHAR(100)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabela 'public.users_info' criada/verificada com sucesso.")

def gerar_dados(qtd=1000):
    fake = Faker("pt_BR")
    return [
        (
            fake.name(),
            fake.email(),
            fake.random_int(min=18, max=80),
            fake.city()
        )
        for _ in range(qtd)
    ]

def inserir_dados(dados):
    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        query = """
            INSERT INTO public.users_info (nome, email, idade, cidade)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (email) DO NOTHING;
        """
        cursor.executemany(query, dados)
        conn.commit()
        cursor.close()
        conn.close()
        print(f"{len(dados)} registos processados com sucesso na camada Raw!")

if __name__ == "__main__":
    criar_tabela()
    dados_gerados = gerar_dados(1000)
    inserir_dados(dados_gerados)