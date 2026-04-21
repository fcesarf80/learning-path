"""
Exercicio 13 - Leia um número e diga se ele é primo (versão simples)
"""
numero = int(input("Digite um número: "))
if numero < 2 or (numero > 2 and numero % 2 == 0):
    primo = False
else:
    limite = int(numero ** 0.5) + 1
    primo = True    
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            primo = False
            break
if primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")