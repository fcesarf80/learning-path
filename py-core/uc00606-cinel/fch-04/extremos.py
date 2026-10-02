"""
Exercício: Extremos
Enunciado: Recorrendo a uma função, dado um tuplo de palavras, determine o comprimento da palavra mais curta e da palavra mais longa.
"""

def extremos(tuplo):
    menor = len(tuplo[0])
    maior = len(tuplo[0])

    for palavra in tuplo:
        if len(palavra) < menor:
            menor = len(palavra)

        if len(palavra) > maior:
            maior = len(palavra)

    return menor, maior


tuplo = ("Ana", "Carlos", "João", "Alexandre")

menor, maior = extremos(tuplo)

print("Menor:", menor)
print("Maior:", maior)