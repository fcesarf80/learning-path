"""
Exercicio 11 - Leia 3 lados e diga se forma um triângulo
"""
l1 = int(input("Digite o 1º lado: "))
l2 = int(input("Digite o 2º lado: "))
l3 = int(input("Digite o 3º lado: "))

if l1 > 0 and l2 > 0 and l3 > 0:
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        print("Esses valores formam um triângulo")
    else:
        print("Esses valores não formam um triângulo")
else:
    print("Valores inválidos")