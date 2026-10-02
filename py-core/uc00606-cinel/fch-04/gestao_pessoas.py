"""
9 Exercício: Gestão de Pessoas
Enunciado:Crie uma lista de pessoas com nome, idade e sexo. Crie um menu que permita:
Mostrar os nomes.
Mostrar os homens.
Mostrar as mulheres.
Calcular a média das idades.
Mostrar os maiores de idade.
Sair.
"""

pessoas = [("Ana", 20, "F"), ("João", 17, "M"), ("Maria", 25, "F"),("Pedro", 30, "M")]

while True:
    print( "1 - Nomes", "2 - Homens", "3 - Mulheres",
    "4 - Média idades", "5 - Maior idade", "0 - Sair", sep="\n")



    op = input("Opção: ")

    if op == "1":
        for p in pessoas:
            print(p[0])

    elif op == "2":
        for p in pessoas:
            if p[2] == "M":
                print(p[0])

    elif op == "3":
        for p in pessoas:
            if p[2] == "F":
                print(p[0])

    elif op == "4":
        soma = 0
        for p in pessoas:
            soma += p[1]
        print("Média:", soma / len(pessoas))

    elif op == "5":
        for p in pessoas:
            if p[1] >= 18:
                print(p[0])

    elif op == "0":
        break