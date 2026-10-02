"""
4 Exercício: Transformação de Tuplos
Enunciado: Recorrendo a funções, crie funções que permitam:
substituir um valor por outro;
duplicar os elementos;
colocar primeiro os elementos das posições pares e depois os das posições ímpares.
"""

def substituir(tuplo, antigo, novo):
    resultado = ()
    for x in tuplo:
        if x == antigo:
            resultado += (novo,)
        else:
            resultado += (x,)
    return resultado


def duplicar(tuplo):
    resultado = ()
    for x in tuplo:
        resultado += (x, x)
    return resultado


def odd_even(tuplo):
    odd, even = (), ()
    
    for i, elem in enumerate(tuplo):
        if i % 2 == 0: 
            even += (elem,)
        else:
            odd += (elem,)

    return even + odd

tuplo = (1, 2, 3, 4, 5)

print("Original:", tuplo)
print("Substituído:", substituir(tuplo, 2, 9))
print("Duplicado:", duplicar(tuplo))
print("Pares/Ímpares:", odd_even(tuplo))
