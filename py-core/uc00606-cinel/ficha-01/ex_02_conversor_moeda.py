"""
Exercício 02 - Conversor de moeda
Enunciado: Fazer um conversor em que dado o valor de euros e a taxa de câmbio, determine o valor em dólar.
"""
# simplified form:   (1€ - taxa / valor - x?)
# taxa = float(input("Qual a taxa de conversão? "))
# valor = float(input("Qual o montante de € a converter? "))
# print(f"{valor:.2f}€ corresponde a {valor*taxa:.2f}$")
def conversor():
    while True:
        try:
            #Pedir os dados ao utilizador
            euros = float(input("\nDigite o valor em Euros (€): "))
            taxa = float(input("Digite a taxa de câmbio (1€ = ? $): "))

            #Calcular e exibir o resultado
            dolares = euros * taxa
            print(f"Resultado: {euros:.2f}€ equivale a ${dolares:.2f}")

        except ValueError:
            print("Erro: Por favor, insira apenas valores numéricos.")
            continue

        #Perguntar se deseja continuar
        pergunta = input("\nDeseja testar outros valores? (s/n): ").lower()
        if pergunta != 's':
            print("Conversor encerrado. Até à próxima!")
            break
