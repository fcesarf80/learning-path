"""
Exercício: Potência e Fatorial
Enunciado: Recorrendo a funções e ciclos, calcule a potência de uma base por um expoente e o fatorial de um número.
"""

def potencia(base, expoente):
    resultado = 1

    for i in range(expoente):
        resultado *= base

    return resultado


def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


base = int(input("Base: "))
expoente = int(input("Expoente: "))
numero = int(input("Número: "))

print("Potência:", potencia(base, expoente))
print("Fatorial:", fatorial(numero))