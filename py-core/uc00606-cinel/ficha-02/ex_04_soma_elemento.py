"""
Exercício 4 – Soma elementos
Enunciado: 4. Faça um programa que dado um tuplo, apresente a soma dos seus elementos.
"""
from random import randint
tup = ()
soma = 0
for _ in range(1,11):
    tup = tup + (randint(1,100),)
    soma = soma + tup[-1]
    print(f"{tup[-1]} foi gerado na iteração nº {_} ")

print(tup)
#somar os elementos da tupla:
print(f"A soma dos elementos da tupla é {soma}")
