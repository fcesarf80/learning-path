"""
exercício 06 - Leia 3 números e mostre o maior
"""
while True:
    # Sua lógica original
    n1 = int(input("Leia o 1º número: "))
    n2 = int(input("Leia o 2º número: "))
    n3 = int(input("Leia o 3º número: "))

    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3 # Corrigi aqui: antes estava maior = 3

    print(f"O maior número é {maior}")

    # Pergunta se o usuário quer continuar
    continuar = input("\nDeseja testar outros valores? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa...")
        break