import sqlite3
import time
import getpass

start_time = time.time()

username = input("Nome de utilizador: ")
password_input = getpass.getpass("Password: ") 

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT password FROM users WHERE name = ?", (username,))
resultado = cursor.fetchone()

if resultado is None:
    print("Utilizador não encontrado. Tenta outra vez.")
    autenticado = False
else:
    
    password_input = getpass.getpass("Password: ")
    password_correta = resultado[0]

    if password_input == password_correta:
        print("Autenticado com sucesso.")
        autenticado = True
    else:
        print("Password incorreta.")
        autenticado = False



end_time = time.time()
tempo_total = end_time - start_time

print("Autenticação:", autenticado)
print(f"Tempo total: {tempo_total:.4f} segundos")

conn.close()
