"""
8 Exercício: Análise de Strings
Enunciado: Recorrendo a uma função, analise uma frase e apresente o número total de caracteres, de letras maiúsculas, de letras minúsculas e de algarismos.
"""

def analisar(frase):
    mai, min, num = 0, 0, 0 

    for char in frase:
        if char.isupper():
            mai += 1
        elif char.islower():
            min += 1
        elif char.isdigit():
            num += 1

    return len(frase), mai, min, num


frase = input("Digite uma frase: ")

total, mai, min, num = analisar(frase)

print(f"Total de caracteres: {total}\nAlgarismos encontrados: {num}")

print(f"Letras Maiúsculas: {mai}\nLetras Minúsculas: {min}")