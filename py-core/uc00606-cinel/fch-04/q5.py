"""
5) Utilizando a função randint da biblioteca random, construa uma lista de 10 valores com números aleatórios entre 0 e 10. Apresente a média dos valores da lista apresentada no ecrã arredondada a 1 casa decimal. Utilize a função round() para realizar o arredondamento.
"""

from random import randint
lst = []
for i in range(10):
    lst.append(randint(0, 10))
med = sum(lst) / len(lst)
print("Lista:", lst, "\nMédia:", round(med, 1))