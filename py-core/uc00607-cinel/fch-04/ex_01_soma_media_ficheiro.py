"""
Exercício 01 - Soma media ficheiro
Enunciado: Cria um programa que:
• Leia um ficheiro numeros.txt (1 número por cada linha do ficheiro)
• Some todos os números
• Mostre o total da soma e apresente a média desses valores no ecrã
"""
ficheiro = open("numeros.txt", "r")
soma = 0
quantidade = 0
for linha in ficheiro:
    numero = float(linha)    
    soma = soma + numero
    quantidade += 1
ficheiro.close()
if quantidade > 0:
    media = soma / quantidade
    print("Total da soma:", soma)
    print("Média dos valores:", media)
else:
    print("O ficheiro está vazio.")