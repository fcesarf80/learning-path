"""
Exercício: Tipos Primitivos
Enunciado: Leia um valor introduzido pelo utilizador e apresente o seu tipo e o resultado dos métodos isnumeric(), isalnum(), isalpha(), isupper(), islower() e istitle().
"""
valor = input("Digite um valor: ")

print("Tipo:", type(valor))
print("Numérico:", valor.isnumeric())
print("Alfanumérico:", valor.isalnum())
print("Alfabético:", valor.isalpha())
print("Maiúsculo:", valor.isupper())
print("Minúsculo:", valor.islower())
print("Título:", valor.istitle())