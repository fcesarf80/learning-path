"""
Exercício 06 - Biblioteca math operacoes
Enunciado: Importando a biblioteca de matemática (math) e lendo um valor float, apresente como resultado:
a. o valor truncado             d. a raiz quadrada do valor arredondado
b. o valor arredondado          e. o fatorial do número arredondado ao inteiro seguinte
c. o cubo do valor truncado
"""

#import math
from math import trunc, sqrt, factorial, ceil
valor = float(input("Insira um valor positivo: "))

#a. o valor truncado,
vtrunc = trunc(valor)
print(f"o valor truncado é {vtrunc}")

#b. o valor arredondado
varred = round(valor)
print(f"o valor arredondado é {varred}")

#c. o cubo do valor truncado
cubo = pow(vtrunc, 3)
print(f"Valor truncado({vtrunc}) elevado a 3 é {cubo}")


#d. a raiz quadrada do valor arredondado
rq = sqrt(varred)
print(f"Raiz quadrada de {varred} é {rq}")

#e. o fatorial do número arredondado ao inteiro seguinte
fat = factorial(ceil(valor))
print(f"Fatorial do valor arredondado por excesso({ceil(valor)}) é {fat}")
