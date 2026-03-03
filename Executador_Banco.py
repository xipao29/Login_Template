import sqlite3

conexao = sqlite3.connect("banco_filmes.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS banco_filmes (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               password TEXT NOT NULL
               )""")

conexao.commit()