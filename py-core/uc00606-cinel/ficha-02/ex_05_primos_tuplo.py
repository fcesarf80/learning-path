"""
Exercício 5 – Elementosprimos tuplo
Enunciado: 5. Faça um script, recorrendo a funções, que dado um tuplo, retorne os elementos primos que aí existem.
"""

from math import ceil 
from random import randint
def verifica(num):
    # 1 e o proprio número são 2 divisores de num
    # sabemos que existe pelomenos esses 2
    # vamos procurar o 3º divisor (se existe tem que estar ate sqrt(num))
    lim = ceil(num ** 0.5 + 1)
    for x in range(2, lim):
        if num % x == 0: #encontrou o 3º divisor. Não é primo
            return False
    return True

def primos(tup):
    tprimos = () #para guardar os primos encontrados
    for elem in tup:
        if verifica(elem) == True: #verifica() devolve True se elem
            tprimos = tprimos + (elem,)    
    return tprimos

tup = () #Tuple vazia
for _ in range(20): # repete 20 vezes
    n = randint(2,100)
    tup = tup + (n, ) #Não tem que ter o formato de tupla
    print(tup)

    resp = primos(tup) #Primos() retorna tupla com valores primos 
    print(f"Os primeiros da tupla são: {resp}.")
