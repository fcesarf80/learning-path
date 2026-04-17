"""
Exercício 01 - Par ou ímpar
Enunciado: Leia um número e mostre: “Par” ou “Ímpar”
"""
num = int(input("Digite um número: "))
res = "par" if num % 2 == 0 else "ímpar"
print(f"O número {num} é {res}")