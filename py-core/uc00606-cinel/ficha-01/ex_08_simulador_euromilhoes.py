"""
Exercício 08 - Simulador Euromilhoes
Enunciado: Implemente uma versão primária do concurso do euromilhões.
Cinco valores entre 1 e 50 e 2 valores entre 1 e 12.
"""

from random import randint, sample
from time import sleep
#valores = sample(range(1, 50), 5)
#estrelas = sample(range(1,12),2)

print("E os números são: ", end=" ")
for _ in range(5):
  valor = randint(1, 50)
  print(valor, end=" ")
  sleep(1)

print("\n\nE as estrelas são: ", end=" ")
for _ in range(2):
  valor = randint(1, 12)
  print(valor, end=" ")
  sleep(1)