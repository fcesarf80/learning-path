"""
Exercício 12 – Unicos aleatorios
Enunciado: 12. Dada uma lista de 20 valores, gerada aleatoriamente com valores
inteiros entre 10 e 20, pretende-se obter uma nova lista sem valores repetidos.
"""

from random import randint
nums = []
for _ in range(20):
    nums.append(randint(10,20))

print(f"A lista gerada é:{nums}")

nova = []
for elem in nums:
    if elem not in nova:
        nova.append(elem)
print(f"Sem repetidos: {nova}")
