"""
Exercício 01 - Soma media ficheiro
Enunciado: Cria um programa que leia um ficheiro "numeros.txt"
(1 número por cada linha do ficheiro), some todos os números e
mostre o total da soma e apresente a média desses valores no ecrã
"""
with open("numeros.txt", "w") as f:
    f.write("10\n20\n30\n40\n50\n")
with open("numeros.txt", "r") as f:
    numeros = [int(linha) for linha in f]
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade
print(f"Soma total: {soma} | Média: {media}")