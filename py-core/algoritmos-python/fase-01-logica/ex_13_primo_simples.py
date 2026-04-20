"""
Exercicio 13 - Leia um número e diga se ele é primo (versão simples)
"""
numero = int(input("Digite um número: "))
limite = int(numero ** 0.5) + 1
primo = True
if numero < 2:
    primo = False
else:
    for divisor in range(2, limite +1):
        if numero % divisor == 0 and numero != divisor:
            primo = False
            break
if primo:
    print(f"{numero} é primo")    
else:
    print(f"{numero} não é primo")