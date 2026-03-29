"""
Exercício 04 - Operações percentuais simples
Enunciado: Dado um preço de um artigo de uma loja e a percentagem do desconto, devolva como resposta o valor final a pagar.
"""

def calcular_desconto():
    while True:
        try:
            # Entrada de dados
            preco_original = float(input("\nDigite o preço do artigo (€): "))
            percentagem_desconto = float(input("Digite a percentagem de desconto (%): "))

            # Cálculos
            valor_desconto = preco_original * (percentagem_desconto / 100)
            preco_final = preco_original - valor_desconto

            # Exibição do resultado
            print(f"Valor do desconto: {valor_desconto:.2f}€")
            print(f"Valor final a pagar: {preco_final:.2f}€")

        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos (use ponto para decimais).")
            continue

        # Pergunta ao utilizador se deseja continuar
        continuar = input("\nDeseja analisar outros valores? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado. Boas compras!")
            break

# Iniciar o programa
if __name__ == "__main__":
    calcular_desconto() 