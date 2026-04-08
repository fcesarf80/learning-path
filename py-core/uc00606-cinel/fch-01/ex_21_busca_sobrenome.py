"""
Exercício 21 - Busca sobrenome
Enunciado: Crie uma função que recebe como argumento o nome de uma pessoa e diga se tem “Coelho” no nome.
"""

def tem_coelho(nome_completo):
    # .lower() evita que o programa ignore "COELHO" ou "coelho"
    if "coelho" in nome_completo.lower():
        return True
    else:
        return False

# Esta parte deve estar encostada na margem esquerda (sem espaços)
if __name__ == "__main__":
    try:
        entrada = input("Digite o nome completo: ")

        if tem_coelho(entrada):
            print("Sim! Existe 'Coelho' no nome.")
        else:
            print("Não foi encontrado 'Coelho' no nome.")

        # Linha para manter a janela aberta se estiver no Windows
        input("\nFim do programa. Pressione Enter para fechar.")

    except EOFError:
        print("\nErro: O terminal não conseguiu ler a entrada.")