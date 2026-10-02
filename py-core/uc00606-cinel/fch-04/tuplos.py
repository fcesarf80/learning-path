"""
Exercício Tuplos
Enunciado: Recorrendo a funções, crie um tuplo com 10 números inteiros. Apresente os seus elementos, calcule a soma e separe os números pares e ímpares em dois novos tuplos.
"""

def criar_tuplo():
    tuplo = ()

    for i in range(10):
        num = int(input("Digite um número: "))
        tuplo += (num,)

    return tuplo


def soma(tuplo):
    total = 0

    for num in tuplo:
        total += num

    return total


def pares_impares(tuplo):
    pares = ()
    impares = ()

    for num in tuplo:
        if num % 2 == 0:
            pares += (num,)
        else:
            impares += (num,)

    return pares, impares


tuplo = criar_tuplo()

print("Tuplo:", tuplo)
print("Soma:", soma(tuplo))

pares, impares = pares_impares(tuplo)

print("Pares:", pares)
print("Ímpares:", impares)