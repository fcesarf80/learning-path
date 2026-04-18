"""
exercício 10 - Leia um número e diga: divisível por 3 e 5, Só por 3, Só por 5 ou Nenhum
"""
num = int(input("Digite um número: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} é divisível por 3 e por 5")
elif num % 3 == 0:
    print(f"{num} é divisível somente por 3")
elif num % 5 == 0:
    print(f"{num} é divisível somente por 5")
else:
    print(f"{num} é não é divisível por 3 nem por 5")
