"""
Exercício: Números Triangulares
Enunciado: Recorrendo a funções, determine se um número é triangular. Um número é triangular quando pode ser escrito como a soma dos primeiros números naturais consecutivos.
"""
def triangular(n):
    soma = 0
    i = 1

    while soma < n:
        soma += i
        i += 1

    return soma == n


n = int(input("Número: "))

if triangular(n):
    print("É triangular.")
else:
    print("Não é triangular.")