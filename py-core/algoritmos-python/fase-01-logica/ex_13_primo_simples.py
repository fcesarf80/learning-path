"""
Exercicio 13 - Leia um número e diga se ele é primo (versão simples)
"""
numero = int(input("Digite um número: "))
if numero < 2 or (numero > 2 and numero % 2 == 0):
    primo = False
elif numero == 2:
    primo = True
else:
    primo = True
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 2
if primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
