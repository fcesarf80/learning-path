"""
Exercício 14 - Número Triangular.
Enunciado: Escreva uma função que dado um número n, verifique se este é triangular.
Um número n diz-se triangular se existir um outro número, menor que n tal que n = 1+2+3+…+m.
A função deverá devolver True se n é triangular e False caso contrário.
"""

def eh_triangular(n):
    if n < 1:
        return False
    soma = 0
    m = 1
    while soma < n:
        soma += m
        m += 1
    return soma == n

def menu_principal():
    while True:
        try:
            # Solicita a entrada do usuário
            numero = int(input("\nDigite um número para verificar se ele é triangular: "))

            if eh_triangular(numero):
                print(f"O número {numero} é triangular!")
            else:
                print(f"O número {numero} NÃO é triangular.")

            # Pergunta se o usuário deseja continuar
            opcao = input("Deseja testar outro número? (S/N): ").strip().lower()

            # Uso do método .startswith() para verificar a resposta
            if not opcao.startswith('s'):
                print("Encerrando o programa...")
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")
# Executa o programa
if __name__ == "__main__":
    menu_principal()