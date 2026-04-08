"""
Exercício 15 – Analise estatistica completa
Enunciado: 15. Construa uma lista com 10 valores inteiros entre 1 e 10, aleatórios.
Apresente essa lista ao utilizador. O programa deverá indicar:
a. Quantos elementos tem a lista (utilize a função len())
b. Apresente o máximo e mínimo da lista (utilize as funções max() e min())
c. Indique a soma de todos os elementos da lista (utilize a função sum())
d. Apresente a média de valores da lista, arredondada a 1 casa decimal.
"""

from random import randint
#Valores gerados aleatoriamente entre 1 e 10
lista = []
for _ in range(10):
    lista.append(randint(1,20))
print(f"A lista gerada foi: {lista}")

#a. Quantos elementos tem a lista (utilize a função len())
print(f"A lista contém {len(lista)} de elementos")

#b. Apresente o máximo e mínimo da lista (utilize as funções max() e min())
print(f"O máximo da lista é {max(lista)} e o minimo é {min(lista)}")

#c. Indique a soma de todos os elementos da lista (utilize a função sum())
print(f"A soma dos elementos da lista é {sum(lista)}")

#d. Apresente a média de valores da lista, arredondada a 1 casa decimal.
print(f"A média é {sum(lista)/len(lista):.1f}")
