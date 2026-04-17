"""
Exercício 02 - Positivo negativo
"""
num = int(input("Digite um número: "))
if num > 0:
    res = "positivo"
elif num < 0:
    res = "negativo"
else:
    res = "zero"
print(f"O número {num} é {res}")