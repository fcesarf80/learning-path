"""
Exercício 1 - Manipulação de Tuplos e Imutabilidade.
Enunciado: 1. Leia 10 valores do STDIN para um tuplo.
"""

tup = () #tupla vazia
for _ in range(10):
    num = int(input("Insira um nº: "))
    tup = tup + (num,) #precisa representar o num como tupla

print(f"A tupla final é {tup}")