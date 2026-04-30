"""
Exercício 03 - Analise preços produtos
Enunciado: Cria um programa que: leia um ficheiro produtos.txt no formato 'nome;preco', guarde os dados num dicionário, mostre o produto mais caro e o mais barato
"""
with open("produtos.txt", "w", encoding="utf-8") as f:
    f.write("Cachimbo do Saci;15.50\nCesto da Cuca;42.00\nPena da Iara;10.00\n")
    f.write("Chapéu do Boto;25.00\nLanterna do Tutu;30.00\n")
# Dividindo a linha 7 em duas partes:
linhas = [lin.strip().split(';') for lin in open('produtos.txt', encoding="utf-8")]
d = {nome: float(preco) for nome, preco in linhas}
print(f"Mais caro: {max(d, key=d.get)} ({d[max(d, key=d.get)]}€)")
print(f"Mais barato: {min(d, key=d.get)} ({d[min(d, key=d.get)]}€)")
