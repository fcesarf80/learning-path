import mysql.connector as liga

def ligacao():
    servidor = "localhost"
    bd = "login"
    nome = "root"
    senha = ""
    try:
        conexao = liga.connect(host=servidor, user=nome,
                               password=senha)
        return conexao

    except liga.Error as erro:
        return None