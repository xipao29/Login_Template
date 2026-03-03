# Importações e Declarações

import customtkinter as ct; import sqlite3

# Conexão com Banco de Dados

conexao = sqlite3.connect("banco_filmes.db")
cursor = conexao.cursor()

# Tela

tela = ct.CTk()
tela.maxsize(height=450, width=350)
tela.minsize(height=450, width=350)
tela.title("Login")

# Grid

tela.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29), weight=1)
tela.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29), weight=1)

# Funções

def switch_log_to_sign():
    global texto_signin
    global texto_login
    global texto_username_2
    global caixa_username
    global caixa_username_2
    global texto_senha
    global texto_senha_2
    global caixa_senha
    global caixa_senha_2
    global botao_login
    global botao_signin
    global botao_switch_login
    global botao_switch_signin

    texto_login.grid_remove()
    texto_username.grid_remove()
    caixa_username.grid_remove()
    texto_senha.grid_remove()
    caixa_senha.grid_remove()
    botao_login.grid_remove()
    botao_switch_signin.grid_remove()

    texto_signin = ct.CTkLabel(tela, text="Signin", font=("Cascadia Code", 19))
    texto_signin.grid(row=4, column=15)

    texto_username_2 = ct.CTkLabel(tela, text="Username", font=("Cascadia Code", 18))
    texto_username_2.grid(row=8, column=15, pady=0.1)

    caixa_username_2 = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
    caixa_username_2.grid(row=9, column=15, pady=0.1)

    texto_senha_2 = ct.CTkLabel(tela, text="Password", font=("Cascadia Code", 18))
    texto_senha_2.grid(row=13, column=15, pady=0.1)

    caixa_senha_2 = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
    caixa_senha_2.grid(row=15, column=15, pady=0.1)

    botao_signin = ct.CTkButton(tela, text="Signin", corner_radius=1, font=("Cascadia Code", 14), width=180, fg_color="#313131", hover_color="#2B2B2B", command=signar)
    botao_signin.grid(row=20, column=15)

    botao_switch_login = ct.CTkButton(tela, text="Does have an account?", font=("Cascadia Code", 14), fg_color="#242424", hover=False, command=switch_sign_to_log)
    botao_switch_login.grid(row=25, column=15)

    tela.title("Signin")

def switch_sign_to_log():
    global texto_signin
    global texto_login
    global texto_username
    global texto_username_2
    global caixa_username
    global caixa_username_2
    global texto_senha
    global texto_senha_2
    global caixa_senha
    global caixa_senha_2
    global botao_login
    global botao_signin
    global botao_switch_login
    global botao_switch_signin

    texto_signin.grid_remove()
    texto_username_2.grid_remove()
    caixa_username_2.grid_remove()
    texto_senha_2.grid_remove()
    caixa_senha_2.grid_remove()
    botao_signin.grid_remove()
    botao_switch_login.grid_remove()

    texto_login = ct.CTkLabel(tela, text="Login", font=("Cascadia Code", 19))
    texto_login.grid(row=4, column= 15)

    texto_username = ct.CTkLabel(tela, text="Username", font=("Cascadia Code", 18))
    texto_username.grid(row=8, column=15, pady=0.1)

    caixa_username = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
    caixa_username.grid(row=9, column=15, pady=0.1)

    texto_senha = ct.CTkLabel(tela, text="Password", font=("Cascadia Code", 18))
    texto_senha.grid(row=13, column=15, pady=0.1)

    caixa_senha = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
    caixa_senha.grid(row=15, column=15, pady=0.1)

    botao_login = ct.CTkButton(tela, text="Login", corner_radius=1, font=("Cascadia Code", 14), width=180, fg_color="#313131", hover_color="#2B2B2B", command=logar)
    botao_login.grid(row=20, column=15)

    botao_switch_signin = ct.CTkButton(tela, text="Does not have an account?", font=("Cascadia Code", 14), fg_color="#242424", hover=False, command=switch_log_to_sign)
    botao_switch_signin.grid(row=25, column=15)

    tela.title("Login")

def logar():
    respota_caixa_username = caixa_username.get()
    resposta_caixa_senha = caixa_senha.get()
    cursor.execute(f"""SELECT id FROM banco_filmes 
                   WHERE username = ? AND password = ?""", (respota_caixa_username, resposta_caixa_senha))
    resultado = cursor.fetchone()

    if resultado:
        texto_login.grid_remove()
        texto_senha.grid_remove()
        texto_username.grid_remove()
        caixa_username.grid_remove()
        caixa_senha.grid_remove()
        botao_login.grid_remove()
        botao_switch_signin.grid_remove()
        texto_username_2.grid_remove()

        # COLOCAR OS ELEMENTOS DO USUARIO AQUI !!!

def signar():
    resposta_caixa_username_2 = caixa_username_2.get()
    reposta_caixa_senha_2 = caixa_senha_2.get()
    cursor.execute(f"""INSERT INTO banco_filmes
                   (username, password) VALUES
                   (?, ?)""", (resposta_caixa_username_2, reposta_caixa_senha_2))
    cursor.fetchall()
    conexao.commit()

# Widgets

texto_username_2 = ct.CTkLabel(tela, text="Username", font=("Cascadia Code", 18))
texto_username_2.grid(row=8, column=15, pady=0.1)

texto_username_2.grid_remove()

texto_login = ct.CTkLabel(tela, text="Login", font=("Cascadia Code", 19))
texto_login.grid(row=4, column= 15)

texto_username = ct.CTkLabel(tela, text="Username", font=("Cascadia Code", 18))
texto_username.grid(row=8, column=15, pady=0.1)

caixa_username = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
caixa_username.grid(row=9, column=15, pady=0.1)

texto_senha = ct.CTkLabel(tela, text="Password", font=("Cascadia Code", 18))
texto_senha.grid(row=13, column=15, pady=0.1)

caixa_senha = ct.CTkEntry(tela, width=250, corner_radius=1, border_width=1, fg_color="#313131", font=("Cascadia Code", 14))
caixa_senha.grid(row=15, column=15, pady=0.1)

botao_login = ct.CTkButton(tela, text="Login", corner_radius=1, font=("Cascadia Code", 14), width=180, fg_color="#313131", hover_color="#2B2B2B", command=logar)
botao_login.grid(row=20, column=15)

botao_switch_signin = ct.CTkButton(tela, text="Does not have an account?", font=("Cascadia Code", 14), fg_color="#242424", hover=False, command=switch_log_to_sign)
botao_switch_signin.grid(row=25, column=15)

# Funcionamento do Programa

tela.mainloop()

conexao.commit()