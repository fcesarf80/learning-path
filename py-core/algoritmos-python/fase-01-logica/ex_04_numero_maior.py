"""
Exercício 04 - número maior
"""
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
print(f"O número {maior} é maior do que o {menor}")