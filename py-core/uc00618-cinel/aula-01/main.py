# 1. Importa o ficheiro correto pelo nome do ficheiro (sem o .py)
import database_connection as li

nome = input("Qual o username? ").strip().lower()
senha = input("Qual a password? ")

# 2. Usa o alias 'li' para chamar a função 'ligacao' que está lá dentro
con = liga.ligacao()  #con irá ficar com apontadorpara
                      #o driver ou recebe None se não fez a ligação

if not con: 
    print("Não foi possível ligar com o servidor de BDs")
    exit()

cursos = con.cursor() # cria a zona intermedia para troca de dados

sql = "selct * from utilizador where none = '{nome}' and senha = {senha}";

cursos.execute(sql)

resposta = cursos.fetchone()
if resposta:
    print(resposta)
else:
    print("Não existe utilizadores registrados com essas credenciais")

print(resposta)