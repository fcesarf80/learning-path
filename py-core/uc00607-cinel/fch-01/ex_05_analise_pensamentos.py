"""
Exercício 5 - Analise pensamentos
Enunciado: Através das ferramentas disponíveis no seu sistema operativo (ex: bloco de notas),
crie um ficheiro com o seguinte texto cujo nome seja pensamentos.txt:

Falar é fácil. Mostre-me o código. (Linus Torvalds)
Não é a linguagem de programação que define o programador, mas sim sua lógica.
Faça como um programador. Quando tudo está errado e confuso, apague tudo e recomece do zero.
Linguagens não morrem mas sim seus programadores.
Uma linguagem não faz seu código ser bom, programadores bons fazem seu código ser bom.
a. Faça um programa que leia o ficheiro anterior e devolva quantas linhas, palavras, vogais e consoantes contém esse ficheiro.
b. Solicite uma palavra ao utilizador e informe-o de quantas vezes essa palavra ocorre no ficheiro e em que nº da linha.
"""

# 1. Leitura do ficheiro (Necessário para a variável 'cont' existir)
# Em vez de apenas "pensamentos.txt"
with open("fch-01/pensamentos.txt", "r", encoding="utf-8") as fp:

    cont = fp.read().splitlines() # splitlines() é mais limpo que split("\n")

# --- PARTE A (Contagens gerais) ---
qt_pals = 0
qtvog, qtcons = 0, 0
vogais = "aáàãâeéêiíoóõôuú"

for linha in cont:
    qt_pals += len(linha.split())
    for car in linha:
        if car.lower() in vogais:
            qtvog += 1
        elif car.isalpha():
            qtcons += 1

print(f"Linhas: {len(cont)} | Palavras: {qt_pals} | Vogais: {qtvog} | Consoantes: {qtcons}")

# --- PARTE B (Busca exata que você ajustou) ---
palavra_busca = input("Qual a palavra a procurar no ficheiro? ").lower()
linhas_onde_ocorre = []
total_ocorrencias = 0

for num_linha, linha in enumerate(cont, start=1):
    # Limpeza para capturar palavras coladas em pontuação
    linha_limpa = linha.replace(".", "").replace(",", "").replace("(", "").replace(")", "")
    palavras_da_linha = linha_limpa.lower().split()
    
    if palavra_busca in palavras_da_linha:
        linhas_onde_ocorre.append(num_linha)
        total_ocorrencias += palavras_da_linha.count(palavra_busca)

print(f"A palavra «{palavra_busca}» ocorre {total_ocorrencias} vezes nas linhas: {linhas_onde_ocorre}")
