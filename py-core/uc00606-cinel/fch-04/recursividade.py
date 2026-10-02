"""
Exercício: Recursividade
Enunciado: Recorrendo a funções recursivas, calcule o fatorial de um número e a potência de uma base por um expoente.
"""

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)


def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)


n = int(input("Número: "))
base = int(input("Base: "))
expoente = int(input("Expoente: "))

print("Fatorial:", fatorial(n))
print("Potência:", potencia(base, expoente))