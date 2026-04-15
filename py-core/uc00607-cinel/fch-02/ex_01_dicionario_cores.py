"""
Exercício 01 - Dicionario de cores
Enunciado: Considere a seguinte lista de cores: ['Preto', 'Branco', 'Azul',
'Verde', 'Vermelho', 'Amarelo','Castanho', 'Rosa', 'Laranja', 'Cinzento']. 
A partir desta lista, construa um dicionário de cores, onde a chave é a cor
em português (consta da lista) e o valor é a cor correspondente em inglês que
deverá ser solicitada ao utilizador. Após a construção do dicionário, o seu 
programa deverá solicitar ao utilizador qual a cor que deseja traduzir e dar 
como resposta a cor correspondente em Inglês.
Guarde num ficheiro os elementos do dicionário (estrutura: corPT;corING).
"""
# 1. Lista inicial de cores (atualizada para 'Cinza')
lcores = ["Preto", "Branco", "Azul", "Verde", "Vermelho", 
          "Amarelo", "Castanho", "Rosa", "Laranja", "Cinza"]
# 2. Construção do dicionário solicitando traduções
dcores = {}
print("--- Fase 1: Construção do Dicionário ---")
for cor in lcores:
    cor_ing = input(f"Qual a tradução para {cor}? ").strip().title()
    dcores[cor] = cor_ing
# 3. Consulta de tradução
print("\n--- Fase 2: Consulta de Cores ---")
while True:
    cor_busca = input("Qual a cor que deseja traduzir? (0 - SAIR): ").strip().title()
    
    if cor_busca == "0":
        break
    
    if cor_busca in dcores:
        print(f"Resposta: {cor_busca} -> {dcores[cor_busca]}")
    else:
        print(f"A cor '{cor_busca}' não foi encontrada.")

# 4. Gravação no ficheiro (Estrutura: corPT;corING)
with open("dicING.csv", "w", encoding="utf-8") as fp:
    for pt, ing in dcores.items():
        fp.write(f"{pt};{ing}\n")

print("\nFicheiro 'dicING.csv' guardado com sucesso!")