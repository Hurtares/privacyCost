import sqlite3
import hashlib
import time
import random

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT name, password FROM users")
utilizadores_originais = cursor.fetchall()

random.shuffle(utilizadores_originais)

start_time = time.time()

total_testes = 0
sucesso = 0
falha = 0

for nome, password in utilizadores_originais:
    hash_ger = hash_password(password)

    cursor.execute("SELECT password FROM User_Sha256 WHERE name = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        hash_na_bd = resultado[0]
        if hash_na_bd == hash_ger:
            sucesso += 1
        else:
            falha += 1
    else:
        falha += 1  

    total_testes += 1


end_time = time.time()
tempo_total = end_time - start_time


print(f"Total de comparações: {total_testes}")
print(f"Autenticações bem-sucedidas: {sucesso}")
print(f"Falhas: {falha}")
print(f"Tempo total: {tempo_total:.4f} segundos")

conn.close()
