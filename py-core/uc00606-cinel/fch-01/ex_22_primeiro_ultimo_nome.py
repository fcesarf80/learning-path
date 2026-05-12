"""
Exercício 22 - Primeiro e ultimo nome
Enunciado: Programa que leia o nome completo de uma pessoa
e mostre o 1º e último nome separados. Ex: Jules Gabriel Verne
1º: Jules | último: Verne
"""


def exibir_primeiro_e_ultimo_nome():
    nome_completo = input("Digite seu nome completo: ").strip()
    nomes_separados = nome_completo.split()

    if len(nomes_separados) > 0:
        primeiro_nome = nomes_separados[0]
        ultimo_nome = nomes_separados[-1]

        print(f"\nMuito prazer em te conhecer!")
        print(f"Seu primeiro nome é: {primeiro_nome}")
        print(f"Seu último nome é: {ultimo_nome}")
    else:
        print("Erro: Você não digitou um nome válido.")


if __name__ == "__main__":
    exibir_primeiro_e_ultimo_nome()
