import sqlite3
import os
from werkzeug.security import generate_password_hash
DATABASE_NAME = "contracts.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            cpf_client TEXT NOT NULL,
            location TEXT NOT NULL,
            cep TEXT,
            rent_value REAL NOT NULL,
            entry_date DATE NOT NULL,
            email TEXT,
            file_path TEXT
        )       
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            user_password TEXT NOT NULL
        )       
    """)
    
    conn.commit()
    conn.close()

    if not os.path.exists("uploads"):
        os.makedirs("uploads")
        print("pasta feita!")
    
def insert_contract(client_name, cpf_client, location, cep, rent_value, entry_date, email, file_path):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contracts (client_name, cpf_client, location, cep, rent_value, entry_date, email, file_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (client_name, cpf_client, location, cep, rent_value, entry_date, email, file_path))
    conn.commit()
    conn.close()

def get_all_contracts():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM contracts
    """)
    results = cursor.fetchall()
    conn.close()
    return results


def insert_user(username, user_password):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, user_password)
        VALUES (?, ?)
        """, (username, generate_password_hash(user_password)))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users WHERE username = ?
    """, (username,))
    results = cursor.fetchone()
    conn.close()
    return results

def get_user_by_id(id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users WHERE id = ?
    """, (id,))
    results = cursor.fetchone()
    conn.close()
    return results



