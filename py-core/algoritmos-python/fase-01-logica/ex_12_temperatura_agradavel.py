"""
Exercicio 12 - Leia temperatura e classifique
"""
temperatura = int(input("Digite a temperatura: "))
if temperatura < 15:
    print("O tempo está frio")
elif temperatura <= 25:
    print("O tempo está agradável")
else:
    print("O tempo está quente") 