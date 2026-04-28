"""
Exercício 04 - Contagem palavras texto
Enunciado: Cria um programa que:
• Leia um ficheiro de texto (qualquer)
• Conte quantas vezes cada palavra aparece
• Mostre as palavras e respetivas contagens
"""
ficheiro = open("texto.txt", "r")
contagem = {}
for linha in ficheiro:
    palavras = linha.lower().split()
    for p in palavras:
        p = p.replace(",", "").replace(".", "")
        if p in contagem:
            contagem[p] += 1 # Atalho aplicado aqui
        else:
            contagem[p] = 1
ficheiro.close()
for p in contagem:
    print(p, ":", contagem[p])