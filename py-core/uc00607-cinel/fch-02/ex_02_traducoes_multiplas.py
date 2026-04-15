"""
Exercício 02 - Traduções multiplas
Enunciado: A partir do arquivo criado no exercício anterior,
carregue o dicionário para memória. Altere o dicionário por 
forma a acrescentar as cores em francês. Assim, o seu dicionário
obteria as traduções de português para inglês e francês.
Espera-se obter o dicionário {Preto: (Black, Noir), Branco: (White, Blanc),
Azul: (Blue, Bleu), Verde: (Green, Vert), Vermelho: (Red, Rouge), 
Amarelo: (Yellow, Jaune), Castanho: (Brown, Marron), Rosa: (Pink, Rose), 
Laranja: (Orange, Orange), Cinzento: (Gray, Gris)} Guarde num arquivo os
elementos do dicionário (estrutura: corPT;corING:corFR).
Sugestão: alterar cada valor do dicionário para uma lista/tupla de valores,
onde o 1º valor é a palavra em inglês (que já lá está) e o 2º valor a palavra
em francês que irá ser solicitada ao utilizador."""

# --- PARTE 1: Carregar dados do arquivo anterior ---
dcores = {}
try:
    with open("dicING.csv", "r", encoding="utf-8") as fp:
        for linha in fp:
            linha = linha.strip()
            if linha and ";" in linha: 
                chave, valor = linha.split(";")
                dcores[chave] = valor
except FileNotFoundError:
    print("Erro: O arquivo 'dicING.csv' não foi encontrado. Corre o Exercício 01 primeiro.")
    exit()
# --- PARTE 2: Adicionar as traduções em Francês ---
print("--- Tradução para Francês ---")
for chave in dcores:
    corING = dcores[chave]
    corFR = input(f"Tradução de «{chave}» para francês? ").strip().title()
    # Atualiza o dicionário para guardar uma tupla (Inglês, Francês)
    dcores[chave] = (corING, corFR)
# --- PARTE 3: Guardar no novo arquivo (corPT;corING;corFR) ---
print("\n--- A gravar novo arquivo 'dicINGFR.csv' ---")
with open("dicINGFR.csv", "w", encoding="utf-8") as fp:
    for chave, (ing, fr) in dcores.items():
        fp.write(f"{chave};{ing};{fr}\n")

print("Dicionário completo: ", dcores)
print("Concluído com sucesso!")