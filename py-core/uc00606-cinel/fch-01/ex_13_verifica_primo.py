"""
Exercício 13 - Verifica primos.
Enunciado:  Recorrendo a funções, determine se um dado número n é primo ou não
"""

def eh_primo(n):
    # --- Verifica se um número n é primo.---
    if n <= 1:
        return False
    # Verifica divisores de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Programa principal
try:
    numero = int(input("Digite um número inteiro: "))

    if eh_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
except ValueError:
    print("Por favor, insira apenas números inteiros.")