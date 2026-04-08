"""
Exercicio 06 - Extremos
Enunciado: 6. Escreva uma função extremos(palavras) que, dada uma tupla palavras
contendo várias cadeias de caracteres, retorne uma tupla (a,b) onde a é o comprimento
da menor cadeia e b é o comprimento da maior cadeia. Restrições: Os seguintes limites
são garantidos em todos os casos de teste que serão dados ao seu programa:
1 ≤ |palavras| ≤ 100  -  número de palavras /  1 ≤ |wi| ≤ 100		tamanho de cada palavra
Ex: print(extremes( ("Alberto", "Francesco", "Miriam", "Pedro", "Tadeu") )) Saída: (5, 9)
Ex: print(extremes( ("c/c++", "java", "python", "prolog", "haskell",) )) Saída: (4, 7)
Ex: print(extremes( ("Portugal", "Espanha", "Itália") ))  Saída:(5, 8)
"""

def extremes(tup):
    tamMax = len(tup[0]) # tamanho da 1ª palavra
    tamMin = tamMax # ou tamMix = len(tup[0])
    for palavra in tup:
        tam = len(palavra)
        if tam < tamMin:
            tamMin = tam
        if tam > tamMax:
            tamMax = tam
    return tamMin, tamMax
tup = ()
qt = int(input("Quantas palavras quer escrever? "))
for x in range(1, qt+1):
    palavra = input(f"Insira a {x}º a palavra: ")
    tup += (palavra,)
print(tup)
resp = extremes(tup)
print(resp)
