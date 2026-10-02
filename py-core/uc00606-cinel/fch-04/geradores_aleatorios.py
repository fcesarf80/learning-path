"""
Exercício: Geradores Aleatórios
Enunciado: Recorrendo a ciclos e à função randint(), apresente 10 números aleatórios entre 20 e 100. De seguida, gere uma chave do Euromilhões com 5 números entre 1 e 50 e 2 estrelas entre 1 e 12.
"""

from random import randint


print("Números aleatórios:")

for i in range(10):
    print(randint(20, 100))


print("Euromilhões:")

numeros = ()

for i in range(5):
    numeros += (randint(1, 50),)

estrelas = ()

for i in range(2):
    estrelas += (randint(1, 12),)

print("Números:", numeros)
print("Estrelas:", estrelas)