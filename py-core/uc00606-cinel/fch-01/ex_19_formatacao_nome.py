"""
Exercício 19 - Formatação nome
Enunciado: Crie um programa que leia o nome completo de um utilizador e mostre:
a) Nome com todas as letras maiúsculas do nome
b) Nome com todas as letras minúsculas
c) Quantas letras tem o nome sem os espaços
d) Quantas letras tem o 1º nome
"""

def analisar_nome():
    # Solicita o nome completo e remove espaços extras no início e fim
    nome_completo = input("Digite seu nome completo: ").strip()
    # a. Nome em maiúsculas
    maiusculas = nome_completo.upper()
    # b. Nome em minúsculas
    minusculas = nome_completo.lower()
    # c. Total de letras sem considerar espaços
    # Removemos todos os espaços internos e contamos o que sobra
    letras_sem_espaco = len(nome_completo.replace(" ", ""))
    # d. Quantas letras tem o primeiro nome
    # Dividimos o nome em uma lista de palavras e pegamos a primeira
    lista_nomes = nome_completo.split()
    primeiro_nome = lista_nomes[0]
    total_primeiro_nome = len(primeiro_nome)
    # Exibição dos resultados
    print(f"\n--- Análise do Nome ---")
    print(f"A. Maiúsculas: {maiusculas}")
    print(f"B. Minúsculas: {minusculas}")
    print(f"C. Total de letras (sem espaços): {letras_sem_espaco}")
    print(f"D. Letras no primeiro nome ({primeiro_nome}): {total_primeiro_nome}")

if __name__ == "__main__":
    analisar_nome()