"""
Exercício 22 - Primeiro e ultimo nome
Enunciado: Programa que leia o nome completo de uma pessoa e mostre o 1º e último nome separados.
Ex: Júlio Guilherme Magalhães
1º: Júlio
último: Magalhães
"""

def exibir_primeiro_e_ultimo_nome():
    # Solicita o nome e remove espaços inúteis nas bordas
    nome_completo = input("Digite seu nome completo: ").strip()

    # Divide o nome em uma lista de palavras usando os espaços como separador
    nomes_separados = nome_completo.split()

    # Verifica se o usuário digitou pelo menos um nome para evitar erros
    if len(nomes_separados) > 0:
        primeiro_nome = nomes_separados[0]
        # O índice -1 em Python sempre pega o último elemento de uma lista
        ultimo_nome = nomes_separados[-1]

        print(f"\nMuito prazer em te conhecer!")
        print(f"Seu primeiro nome é: {primeiro_nome}")
        print(f"Seu último nome é: {ultimo_nome}")
    else:
        print("Erro: Você não digitou um nome válido.")
if __name__ == "__main__":
    exibir_primeiro_e_ultimo_nome()