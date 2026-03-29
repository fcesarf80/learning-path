"""
Exercício 13 – Busca ocorrencias indice
Enunciado: 13. Dada uma sequência de n números e um determinado número x, desenvolva uma função 
que determine a quantidade de vezes que x ocorre na sequência e em que índices da lista se encontra.
"""

from random import randint

#qt de valores dado pelo User
lim = int(input("Qts valores quer gerar? "))
#Valores gerados aleatoriamente entre 1 e 20
lista = []

for _ in range(lim):
    lista.append(randint(1,20))

print(f"A lista gerada foi: {lista}")
x = int(input("Da lista, qual o valor a procurar? "))
qt = 0 #contador
indices = () #tupla para armazenar os indices onde ocorre o X na lista

for pos, elem in enumerate(lista):
    if elem == x: #encontrei
        qt = qt + 1 #encontrei + uma vez o X
        indices = indices + (pos,)

print(f"O valor «{x}» ocorre {qt} vezes e nos índices {indices}")
