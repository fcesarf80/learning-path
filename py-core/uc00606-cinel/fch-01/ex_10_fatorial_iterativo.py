"""
Exercício 10 - Fatoria iterativo.
Enunciado: Dado um valor inteiro positivo, determine a função fatorial.
"""

# 1. Versão Manual (Ciclo for) - é a mais eficiente em termos de memória para números muito grandes, pois não cria várias camadas de funções na memória (pilha de recursão).

def fatorial_manual(n):
    resultado = 1
    # Multiplica todos os números de 1 até n
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Utilização:
try:
    num = int(input("Digite um número inteiro positivo: "))
    if num < 0:
        print("Erro: O fatorial não existe para números negativos.")
    else:
        print(f"O fatorial de {num} é {fatorial_manual(num)}")
except ValueError:
    print("Erro: Digite apenas números inteiros.")

# 2. Versão Recursiva (Lógica Clássica) - é a abordagem que usa o conceito de "dividir para conquistar", onde a função chama-se a si mesma até chegar ao caso base (0 ou 1).
# def fatorial_recursivo(n):
#     # Caso base: o fatorial de 0 ou 1 é 1
#     if n <= 1:
#         return 1
#     # Passo recursivo: n * (n-1)!
#     else:
#         return n * fatorial_recursivo(n - 1)

# # Utilização:
# try:
#     num = int(input("Digite um número: "))
#     if num < 0:
#         print("Erro: Use números positivos.")
#     else:
#         print(f"O fatorial de {num} é {fatorial_recursivo(num)}")
# except ValueError:
#     print("Erro: Entrada inválida.")

# 3. Versão Oficial (Módulo math) - esta é a forma profissional. O módulo math do Python é escrito em C, por isso é extremamente rápido e já trata erros internamente.

# import math

# try:
#     num = int(input("Digite um número: "))
#     # A função math.factorial já faz todo o trabalho pesado
#     resultado = math.factorial(num)
#     print(f"O fatorial de {num} é {resultado}")
# except ValueError:
#     print("Erro: O número deve ser um inteiro positivo.")
