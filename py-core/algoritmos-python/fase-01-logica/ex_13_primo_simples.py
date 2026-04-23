"""
Exercicio 13 - Verificação de número primo (Versão Generalista)
"""
numero = int(input("Digite um número: "))
primo = True
if numero < 2 or (numero % 2 == 0 and numero != 2):
    primo = False
else:
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