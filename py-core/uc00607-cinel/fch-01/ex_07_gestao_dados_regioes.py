"""
Exercício 7 - Gestão dados regiões
Enunciado: Considere o seguinte ficheiro de texto: (ou em formato csv separados por ;)
Ana;Lisboa;22;Centro	      Pedro;Faro;23;Sul	    	Sofia;Viseu;26;Centro
Pedro;Porto;45;Norte	      José;Covilhã;56;Centro	Bruno;Guimarães;34;Norte
Isabel;Coimbra;22;Centro      Marta; Bragança;28;Norte  Helena; Évora;52;Sul
Ana;Chaves;33;Norte	      Luís;Aveiro;39;Centro	Tiago; Coimbra;29;Centro
José;Beja;45;Sul	      Carla;Setúbal;31;Sul	Patrícia;Bragança;41;Norte
Francisco; Bragança;19;Norte  Rui;Évora;47;Sul	    	André;Santarém;38;Centro

a. Quantas pessoas se encontram registadas?
b. Qual a quantidade de pessoas distribuídas pelas zonas do país (Norte, Centro, Sul)?
c. Dada a zona do país, determine a média de idades.
d. Dado o nome de uma pessoa, mostrar onde ela vive (nome da cidade).
   Deve mostrar todas as ocorrências do nome dado.
e. Dada uma cidade, calcular quantas pessoas lá vivem.
f. Qual a cidade com mais habitantes registados no ficheiro?
g. Determinar a quantidade de pessoas em todas as cidades e qual a percentagem correspondente.
h. Dado o nome de uma cidade, perguntar se para a respetiva pessoa, pretende mudar de cidade.
   Se sim, então deve substituir o nome da cidade registado pelo nome da nova cidade.
i. Crie um novo ficheiro com a informação que está em memória, respeitando o formato do csv.
"""

import csv

dados = []
# Lendo o arquivo original
with open('fch-01/texto2_new.csv', 'r', encoding='utf-8') as f:
    for linha in f:
        # Divide a linha por espaços longos (tabs/múltiplos espaços)
        partes = linha.split() 
        for registro in partes:
            # Agora divide cada registro pelo ';'
            campos = registro.split(';')
            if len(campos) == 4:
                dados.append({
                    'nome': campos[0].strip(),
                    'cidade': campos[1].strip(),
                    'idade': int(campos[2]),
                    'regiao': campos[3].strip()
                })

def mudar_cidade(cidade_alvo, dados):
    for p in dados:
        if p['cidade'].lower() == cidade_alvo.lower():
            print(f"Encontrado: {p['nome']} vive em {p['cidade']}.")
            op = input(f"Deseja mudar a cidade de {p['nome']}? (s/n): ")
            if op.lower() == 's':
                p['cidade'] = input("Digite a nova cidade: ")

# a. Quantidade total
print(f"a. Total de pessoas: {len(dados)}")

# b. Pessoas por região
regioes = {}
for p in dados:
    regioes[p['regiao']] = regioes.get(p['regiao'], 0) + 1
print(f"b. Distribuição por região: {regioes}")

# c. Média de idades por zona
soma_idades = {}
for p in dados:
    reg = p['regiao']
    soma_idades.setdefault(reg, []).append(p['idade'])
medias = {reg: sum(ids)/len(ids) for reg, ids in soma_idades.items()}
print(f"c. Média de idades por zona: {medias}")
# d. Dado o nome de uma pessoa, mostrar onde vive (todas as ocorrências)
nome_alvo = input("Digite o nome para saber onde vive: ")
encontrados = [p['cidade'] for p in dados if p['nome'].lower() == nome_alvo.lower()]
print(f"d. {nome_alvo} vive em: {', '.join(encontrados) if encontrados else 'Não encontrado'}")

# e. Dada uma cidade, calcular quantas pessoas lá vivem
cidade_alvo = input("Digite a cidade para contar habitantes: ")
contagem = sum(1 for p in dados if p['cidade'].lower() == cidade_alvo.lower())
print(f"e. Na cidade {cidade_alvo} vivem {contagem} pessoas.")

# f. Cidade com mais habitantes (usando a lógica da alínea g)
contagem_cidades = {}
for p in dados:
    contagem_cidades[p['cidade']] = contagem_cidades.get(p['cidade'], 0) + 1
cidade_max = max(contagem_cidades, key=contagem_cidades.get)
print(f"f. Cidade com mais habitantes: {cidade_max}")

# g. Percentagem por cidade
total = len(dados)
print("g. Quantidade e Percentagem por cidade:")
for cid, qtd in contagem_cidades.items():
    perc = (qtd/total) * 100
    print(f" - {cid}: {qtd} pessoas ({perc:.2f}%)")

# Chamar a função da alínea h
mudar_cidade("Coimbra", dados)

# i. Gravar novo ficheiro final
with open('texto2_final.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f, delimiter=';')
    for p in dados:
        escritor.writerow([p['nome'], p['cidade'], p['idade'], p['regiao']])
