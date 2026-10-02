"""
Exercício: Divisores e MDC
Enunciado: Recorrendo a funções, calcule o máximo divisor comum (MDC) de dois números e a soma dos divisores de um número.
"""

def mdc(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def soma_divisores(n):
    soma = 0

    for i in range(1, n + 1):
        if n % i == 0:
            soma += i

    return soma


n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print("MDC:", mdc(n1, n2))
print("Soma dos divisores do primeiro:", soma_divisores(n1))