"""
Exercício 14 – Ranking maiores numeros
Enunciado: 14. Crie uma lista com 10 números. Implemente uma 
função que determine os 5 maiores números que constam da lista.
"""

from random import randint  # <-- Esta linha é obrigatória no topo

def maiores(nums):
    nums.sort(reverse=True)
    return nums[:5]

nums = []
for _ in range(10):
    nums.append(randint(1, 100)) # Agora o Python já sabe o que é randint

print(f"Lista: {nums}")
print(f"5 maiores: {maiores(nums)}")
