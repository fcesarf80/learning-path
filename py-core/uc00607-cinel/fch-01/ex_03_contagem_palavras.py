"""
Exercício 3 - Contagem palavras
Enunciado: Dado um ficheiro de texto e uma palavra (string) solicitada ao
utilizador, indique quantas vezes ocorre essa palavra (string) no ficheiro.
"""
import string

palavra_busca = input("Qual a palavra que você procurar? ").lower()

try:
    with open("texto.txt", "r", encoding="utf-8") as fp:
        # 1. Lê o texto e coloca tudo em minúsculas
        conteudo = fp.read().lower()
        
        # 2. Cria uma tabela que mapeia cada sinal de pontuação para "nada"
        # string.punctuation contém: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        tabela_limpeza = str.maketrans("", "", string.punctuation)
        conteudo_limpo = conteudo.translate(tabela_limpeza)
        
        # 3. Divide o texto limpo em uma lista de palavras
        palavras = conteudo_limpo.split()
        
    # 4. Conta a ocorrência exata
    qt = palavras.count(palavra_busca)

    if qt == 0:
        print(f"'{palavra_busca}' não foi encontrada.")
    else:
        print(f"'{palavra_busca}' ocorre {qt} {'vez' if qt == 1 else 'vezes'}.")

except FileNotFoundError:
    print("Erro: O arquivo 'texto.txt' não foi encontrado.")