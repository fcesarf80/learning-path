"""
Exercício 01 - Soma media ficheiro
Enunciado: Cria um programa que: • Leia um ficheiro numeros.txt
(1 número por cada linha do ficheiro) • Some todos os números
• Mostre o total da soma e apresente a média desses valores no ecrã
"""
ficheiro = open("numeros.txt", "w")
ficheiro.write("10\n")
ficheiro.write("20\n")
ficheiro.write("30\n")
ficheiro.write("40\n")
ficheiro.write("50\n")
ficheiro.close()
soma = 0
quantidade_numeros = 0
ficheiro = open("numeros.txt", "r")
for linha in ficheiro:
    numero = int(linha)
    soma = soma + numero
    quantidade_numeros = quantidade_numeros + 1
ficheiro.close()
media = soma / quantidade_numeros
print("Soma total:", soma)
print("Média:", media)