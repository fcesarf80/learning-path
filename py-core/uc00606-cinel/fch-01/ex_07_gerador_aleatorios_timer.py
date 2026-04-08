"""
Exercício 07 - Gerador aleatorios timer
Enunciado: Mostrar como output, segundo a segundo, na vertical,
10 valores aleatórios entre 20 e 100.
"""

#import random
from random import randint
from time import sleep

for _ in range(10):
  print(randint(20,100))
  sleep(1.5)