"""
exercício 07 - Leia um número e diga se ele está entre 10 e 50
"""
while True:

    num = int(input("Digite um número: "))
    if 10 <= num <= 50:
        print(f"O número {num} está dentro do intervalo esperado")
    else:
        print(f"O número {num} não está dentro do intervalo esperado")

    continuar = input("\nDeseja testar outros valores? (s/n): ? ").lower()
    if continuar != 's':
        print("Encerrando o programa...")
        break