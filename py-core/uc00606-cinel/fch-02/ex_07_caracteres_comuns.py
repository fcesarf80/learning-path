"""
Exercício 7 – Caracteres comuns strings
Enunciado: 7. Dadas 2 strings, faça um programa que apresente um tuplo com os caracteres comuns de ambas strings.
"""

frase1 = "ola mundo"
conjt1 = set(frase1)
frase2 = "hoje chove"
conjt2 = set(frase2)

intersec = conjt1 & conjt2 #& é interseção de conjuntos
print(intersec)
 #Mostra repetidos se houver
for letra in frase1:  
    if letra in frase2:
        print(letra,end="")
