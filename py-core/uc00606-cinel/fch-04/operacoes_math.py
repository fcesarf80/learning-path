"""
Exercício: Operações com math
Enunciado: Leia um número decimal e apresente a parte inteira, o valor arredondado, o cubo da parte inteira, a raiz quadrada do valor arredondado e o fatorial do valor arredondado para cima.
"""

import math

n = float(input("Digite um número: "))

inteiro = math.trunc(n)
arredondado = round(n)

print("Parte inteira:", inteiro)
print("Arredondado:", arredondado)
print("Cubo:", inteiro ** 3)
print("Raiz:", math.sqrt(arredondado))
print("Fatorial:", math.factorial(math.ceil(n)))