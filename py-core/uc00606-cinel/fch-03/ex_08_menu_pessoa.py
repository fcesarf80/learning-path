"""
exercicio_08_menu_pessoas.py
Enunciado: Considere a seguinte lista de tuplas: 
[ (“Ana”,20,”F”), (“Rui”,17,”M”), (“Eva”,56,”F”), (“Kika”,10,”F”),
(“Ze”,22,”M”),(“Xico”,34,”M”), (“Xana”,21,”F”), (“Bela”,33,”F”) ] 
Cada tupla é constituída por 3 valores, o nome (string), a idade
(inteiro) e o sexo (string). Apresente ao utilizador o seguinte menu: 
1- Mostrar nomes     2- Nomes masculinos     3- Nomes femininos
4- Média das idades  5- Maiores de idade (>=18 anos)   0-	Sair 
1-	Implemente cada opção do menu.
"""
lista = [('Ana', 'Braga'), ('Zé', 'Faro'), ('Nelo', 'Braga'), ('Xica', 'Beja'), ('Rui', 'Braga')]

def mostrar_onde_vive(nome_escolhido):
    for nome, cidade in lista:
        if nome == nome_escolhido:
            print(f"A pessoa {nome} vive em {cidade}")
            return
        
def cidade_cheia():
    contador = {}
    for nome, cidade in lista:
        contador[cidade] = contador.get(cidade, 0) + 1

    vencedora = max(contador, key=contador.get)
    print(f"A cidade com mais gente é: {vencedora}")

def calcular_percentagem(cidade_escolhida):
    total = len(lista)
    conta_cidade = 0
    for nome, cidade in lista:
        if cidade == cidade_escolhida:
            conta_cidade += 1

    resultado = (conta_cidade / total) * 100
    print(f"A cidade {cidade_escolhida} representa {resultado}%")

def remover_pessoa(nome_para_sair):
    lista_nova = []
    for nome, cidade in lista:
        if nome != nome_para_sair:
            lista_nova.append((nome, cidade))
    print(f"Nova lista: {lista_nova}")

nome_input = input("Digite um nome: ")
mostrar_onde_vive(nome_input)

cidade_cheia()
cidade_input = input("Digite uma cidade: ")
calcular_percentagem(cidade_input)

remover = input("Quem quer remover? ")
remover_pessoa(remover)
