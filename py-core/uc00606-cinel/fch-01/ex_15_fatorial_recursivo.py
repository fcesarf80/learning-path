"""
Exercício 15 - Fatorial recursivo
Enunciado: Implemente uma função para cálculo do fatorial de forma recursiva
"""

def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

try:
    # Recebe o valor do usuário
    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Erro: Não existe fatorial de número negativo.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")
