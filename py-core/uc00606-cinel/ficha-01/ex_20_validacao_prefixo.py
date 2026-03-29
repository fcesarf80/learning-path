"""
Exercício 20 - Validação prefixo
Enunciado: Crie uma função que recebe como argumento o nome de uma cidade e diga se ela começa ou não com o nome “Porto”
"""

def verifica_cidade(nome_cidade):
    # Remove espaços em branco extras e ajusta para que a primeira letra seja maiúscula
    # Isso garante que " porto alegre" ou "PORTO" funcionem corretamente
    nome_ajustado = nome_cidade.strip().capitalize()
    # Verifica se a string começa com a palavra "Porto"
    if nome_ajustado.startswith("Porto"):
        return True
    else:
        return False
def programa_principal():
    cidade = input("Digite o nome de uma cidade: ")

    if verifica_cidade(cidade):
        print(f"A cidade '{cidade}' começa com 'Porto'.")
    else:
        print(f"A cidade '{cidade}' NÃO começa com 'Porto'.")

if __name__ == "__main__":
    programa_principal()