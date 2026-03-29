"""
Exercício 01 - Análise de Dados de Entrada
Enunciado: Elabore um script que dado alguma coisa no input, devolva como output:
a. O tipo primitivo;        d. É alfabético?            g. Está capitalizada?
b. É um número?             e. Está em maiúsculas?
c. É alfanumérico?          f. Está em minúsculas?
"""

texto = input("Escreva algo: ")
#a. O tipo primitivo;
print(f"O tipo da variável é {type(texto)}")

#b. É um número?
print(f"É número? {texto.isnumeric()}")

#c. É alfanumérico?
print(f"É alfanumerico? {texto.isalnum()}")

#d. É alfabético?
print(f"É só texto? {texto.isalpha()}")

#e. Está em maiúsculas?
print(f"É tudo maiusculo? {texto.isupper()}")

#f. Está em minúsculas?
print(f"É tudo minusculo? {texto.islower()}")

#g. Está capitalizada?
print(f"Está capitalizado? {texto.istitle()}")