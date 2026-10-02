"""
12 Exercício: Palíndromo e Strings
Enunciado: Recorrendo a funções, verifique se uma palavra é um palíndromo e permita remover todas as ocorrências de um determinado carácter de uma frase.
"""

def palindromo(pal):
    pal = pal.lower()  # 👈 Transforma tudo em minúsculo antes de comparar
    return pal == pal[::-1]


def remover(frase, char):
    res = ""

    for i in frase:
        if i != char:
            res += i

    return res


pal = input("Digite uma palavra: ")

if palindromo(pal):
    print("É palíndromo.")
else:
    print("Não é palíndromo.")


frase = input("Digite uma frase: ")
char = input("Digite o carácter a remover: ")

print("Resultado:", remover(frase, char))

