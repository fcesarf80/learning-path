"""
Exercício: Lista cidades
Enunciado: Crie uma lista com 5 cidades. Recorrendo a funções, permita consultar se uma cidade existe, substituir uma cidade por outra e remover uma cidade.
"""

def criar_lista():
    cidades = []

    for i in range(5):
        cidade = input("Digite uma cidade: ")
        cidades.append(cidade)

    return cidades


def substituir(cidades):
    cidade = input("Cidade a substituir: ")

    if cidade in cidades:
        nova = input("Nova cidade: ")
        posicao = cidades.index(cidade)
        cidades[posicao] = nova
    else:
        print("Cidade não encontrada.")


def remover(cidades):
    cidade = input("Cidade a remover: ")

    if cidade in cidades:
        cidades.remove(cidade)
    else:
        print("Cidade não encontrada.")


cidades = criar_lista()

print(cidades)

substituir(cidades)
print(cidades)

remover(cidades)
print(cidades)