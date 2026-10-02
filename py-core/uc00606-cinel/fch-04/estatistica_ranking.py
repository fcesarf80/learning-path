"""
6 Exercício: Estatistica ranking
Enunciado: Crie uma lista com 10 números inteiros aleatórios entre 1 e 100. Recorrendo a funções, apresente a quantidade de elementos, o maior, o menor, a soma, a média e os 5 maiores valores da lista.
"""

from random import randint

def stats(lst):
   print(f"Qtd: {len(lst)} \nMaior: {max(lst)} | Menor: {min(lst)}")
   print(f"Soma: {sum(lst)} | Média: {round(sum(lst) / len(lst), 1)}")

def top5(lst):
    return sorted(lst, reverse=True)[:5]

lst = [randint(1, 100) for _ in range(10)]

print(f"lista: {lst} | 5 maiores: {top5(lst)}")
stats(lst)