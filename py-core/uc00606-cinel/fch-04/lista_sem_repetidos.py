"""
5 Exercício: Lista sem Repetidos
Enunciado: Crie uma lista com 20 números aleatórios entre 10 e 20. Depois, crie outra lista sem valores repetidos.
"""

from random import randint

lst = []

for i in range(20):
    lst.append(randint(10, 20))

nrpt = []

for num in lst:
    if num not in nrpt:
        nrpt.append(num)

print(f"Lista: {lst} | Sem rep.: {nrpt}")
