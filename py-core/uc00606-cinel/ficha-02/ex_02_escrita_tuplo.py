"""
Exercício 2 – Escrita tuplo
Enunciado: 2. Faça um script que escreva os valores lidos para o tuplo anterior.
"""
from random import randint
tup = () #tupla vazia
for _ in range(10):
    num = randint(1,50) #gera de forma aleatoria num entre 1 e 50
    tup = tup + (num,) #precisa representar o "num" como tupla
print(f"Os elementos da tupla são:")
for elem in tup:
    print(elem, end=" ") 
