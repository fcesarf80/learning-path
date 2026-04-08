"""
Exercício 1 – First last
Enunciado: 1. Escreva uma função first_last(word) que, dada uma string word, retorne uma tupla contendo (a,b,c),
onde a é o seu primeiro caractere, b é o seu último caractere e c é o restante da palavra sem o primeiro e o
último caracteres. Restrições: Os seguintes limites são garantidos em todos os casos de teste que serão dados
ao seu programa:2 ≤ |palavra| ≤ 100 - tamanho da string de entrada
"""

def first_last(frase):
    first = frase[0]
    last = frase[-1]
    seq = frase[1:-1]
    return (first,last,seq)

frase = input("Escreva algo: ")
print(first_last(frase))
