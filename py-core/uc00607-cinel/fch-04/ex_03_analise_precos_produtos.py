"""
Exercício 03 - Analise preços produtos
Enunciado: Cria um programa que: • Leia um ficheiro produtos.txt no formato nome;preco
• Guarde os dados num dicionário • Mostre o produto mais caro • Mostre o mais barato
"""
ficheiro = open("produtos.txt", "r")
produtos = {}
for linha in ficheiro:
    dados = linha.strip().split(";")
    nome = dados[0]
    preco = float(dados[1])
    produtos[nome] = preco
ficheiro.close()

p_caro = ""
p_barato = ""
max_p = -1.0
min_p = 999999.0

for nome in produtos:
    preco = produtos[nome]
    if preco > max_p:
        max_p = preco
        p_caro = nome
    if preco < min_p:
        min_p = preco
        p_barato = nome
print("Mais caro:", p_caro, "| Mais barato:", p_barato)