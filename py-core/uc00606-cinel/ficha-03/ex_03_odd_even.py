"""
Exercicio 3 Odd_even
Enunciado: 3. Escreva uma função odd_even(tup) que, dada uma tupla tup, retorne uma
nova tupla que tenha primeiro todos os valores que estavam em posições ímpares, na
mesma ordem em que estavam originalmente, e depois os valores que estavam em posições
pares, também na mesma ordem. Considere, por exemplo, uma tupla (1,2,3,4,5,6,7,8,9),
na qual o número i está na i-ésima posição, com vermelho para os valores nas posições
ímpares e azul para os pares. Neste caso, a resposta desejada é a tupla (1,3,5,7,9,2,4,6,8),
com os elementos nas posições ímpares vindo primeiro, seguidos pelos pares.
Restrições: Os seguintes limites são garantidos em todos os casos de teste que serão dados
ao seu programa:1 ≤ |tup| ≤ 100 --  tamanho da tupla de entrada
1 ≤ |tup| ≤ 100		--		tamanho da tupla de entrada
Ex: print(odd_even( (1,2,3,4,5,6,7,8) )) - Saída: (1, 3, 5, 7, 2, 4, 6, 8)
Ex: print(odd_even( ("a","b","c","d","e","f") )) - Saída: ('a', 'c', 'e', 'b', 'd', 'f')
Ex: print(odd_even( ("olá", 42, "oh não", 2.0, 14) )) - Saída: ('olá', 'oh não', 14, 42, 2.0)
"""

def odd_even1(tup):
    print("Tupla:", tup)
    odd, even = (), ()
    for i in range(0,len(tup),2):
        even += (tup[i],)
    for i in range(1,len(tup),2):
        odd += (tup[i],)
    return even + odd

def odd_even2(tup):
    print("Tupla:", tup)
    odd, even = (), ()
    for i, elem in enumerate(tup):
        if i%2 == 0: # par
            even = even + (elem,)
        else:
            odd = odd + (elem,)

    return even + odd

def odd_even(tup):
    print("Tupla:", tup)
    odd, even = (), ()
    for i in range(len(tup)):
        if i % 2 == 0:  # par
            even = even + (tup[i],)
        else:
            odd = odd + (tup[i],)

    return even + odd

print(odd_even( ("olá", 42, "oh não", 2.0, 14) ))
