import sqlite3

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("""
    DELETE FROM users
    WHERE id IN (
        SELECT id FROM users ORDER BY id DESC LIMIT 10
    );
""")

conn.commit()
conn.close()

print("Últimos 10 utilizadores removidos com sucesso.")
