"""
Exercício 03 - Menor ou maior idade
"""
idade = int(input("Digite a idade: "))
if idade <= 0:
    res = "idade inválida"
elif idade >= 18:
    res = "maior"
else:
    res = "menor"
print(f"O indivíduo é {res} de idade.")

