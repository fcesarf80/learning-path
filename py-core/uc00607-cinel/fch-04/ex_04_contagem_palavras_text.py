"""
Exercício 04 - Contagem palavras texto
Enunciado: Cria um programa que: leia um ficheiro de texto (qualquer), conte
quantas vezes cada palavra aparece e mostre as palavras e respetivas contagens
"""
from collections import Counter
palavras = Counter(open('texto.txt').read().split())
[print(f"{p}: {c}") for p, c in palavras.items()]