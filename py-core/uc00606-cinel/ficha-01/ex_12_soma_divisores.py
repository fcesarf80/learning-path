"""
Exercício 12 - Soma dos divisores.
Enunciado: Escreva uma função que dado um valor n, determine a soma dos seus divisores. Se o valor inserido for 0 deve devolver 0.
"""

def soma_divisores(n: int) -> int:
    # ---Calcula a soma de todos os divisores de n.---
    n = abs(n)
    soma = 0
    # Percorre de 1 até o próprio número n
    for i in range(1, n + 1):
        if n % i == 0:
            soma += i
    return soma

def executar_programa() -> None:
    print("--- Calculadora de Soma de Divisores ---")

    while True:
        try:
            num = int(input("\nDigite um valor inteiro (ou 0 para sair): "))

            if num == 0:
                print("Valor 0 inserido. Encerrando programa...")
                break

            # Cálculo e exibição
            resultado = soma_divisores(num)

            # Opcional: listar os divisores apenas para verificação
            print(f"-> A soma dos divisores de {num} é: {resultado}")

            # Pergunta se deseja continuar
            continuar = input("\nDeseja testar outro número? (s/n): ").strip().lower()
            if not continuar.startswith('s'):
                print("Programa encerrado.")
                break

        except ValueError:
            print("Erro: Por favor, insira apenas números inteiros.")

if __name__ == "__main__":
    executar_programa()