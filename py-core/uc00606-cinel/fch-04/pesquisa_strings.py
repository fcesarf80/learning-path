"""
Exercício: Pesquisa de Strings
Enunciado: Recorrendo a funções, verifique se uma frase começa por "Porto" e se contém o nome "Coelho".
"""

def verifica_porto(frase):
    return frase.strip().capitalize().startswith("Porto")


def verifica_coelho(frase):
    return "coelho" in frase.lower()


frase = input("Digite uma frase: ")

if verifica_porto(frase):
    print("Começa por Porto.")
else:
    print("Não começa por Porto.")

if verifica_coelho(frase):
    print("Contém Coelho.")
else:
    print("Não contém Coelho.")