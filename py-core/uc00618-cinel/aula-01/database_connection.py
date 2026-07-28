import mysql.connector as liga

def ligacao():
    servidor = "localhost"
    bd = "login"
    nome = "root"
    senha = ""    
    try:
        conexao = liga.connect(host=servidor, database=bd, user=nome, password=senha)
        return conexao
    except liga.Error as erro:
        print(f"Erro detalhado: {erro}")  # Boa prática para saber o motivo se falhar
        return None

# 1. Chama a função apenas UMA vez
minha_conexao = ligacao()

# 2. Verifica o resultado da ligação
if minha_conexao:
    print("Sucesso: Ligação estabelecida com o MySQL!")
    
    # 3. Fecha a ligação de forma segura após o uso
    minha_conexao.close()
    print("Ligação fechada com sucesso.")
else:
    print("Falha: Não foi possível ligar à base de dados.")
