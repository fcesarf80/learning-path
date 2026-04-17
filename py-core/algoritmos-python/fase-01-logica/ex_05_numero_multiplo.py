"""
Exercício 05 - Multiplos de cinco?
"""
num = int(input("Digite um número: "))
if num % 5 == 0: 
    res = "é"
else:
    res = "não é"
print(f"{num} {res} multiplo de 5.")