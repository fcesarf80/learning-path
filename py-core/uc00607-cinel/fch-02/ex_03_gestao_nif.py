"""
Exercício 03 - Gestão NIF
Enunciado:Considere o seguinte ficheiro csv coma seguinte estrutura:
123456789;Ana;Lisboa;22;Centro - 987654321;Pedro;Porto;45;Norte
192837465;Isabel;Coimbra;22;Centro - 564738291;Ana;Chaves;33;Norte
837465192;José;Beja;45;Sul - 748392615;Francisco;Bragança;19;Norte
615294837;Pedro;Faro;23;Sul - 294837156;José;Covilhã;56;Centro
483920176;Marta;Bragança;28;Norte - 572940183;Luís;Aveiro;39;Centro
620481739;Carla;Setúbal;31;Sul - 918273645;Rui;Évora;47;Sul
736291840;Sofia;Viseu;26;Centro - 840192736;Bruno;Guimarães;34;Norte
369258147;Helena;Évora;52;Sul - 501928374;Tiago;Coimbra;29;Centro
210394857;Patrícia;Bragança;41;Norte - 475839102;André;Santarém;38;Centro
Importe o conteúdo do arquivo para um dicionário onde a chave será o
1º campo (NIF).
Os restantes elementos de cada linha deverão ser armazenados como lista
associados à chave NIF.
• Deverá indicar quantos registos foram lidos do arquivo
• Apresente os nomes de todas as pessoas com idade superior a 40 anos
• Construa um dicionário onde guarde a informação de quantas pessoas
existem por zona do país (exemplo: {"Norte": X, "Centro": Y, "Sul": Z})
• Calcule a idade média dos contatos.
• Construa um novo dicionário com a idade média por região
(ex: {"Norte": média1, "Centro": média2, "Sul": média3}
• Criar um dicionário onde a chave é o NIF e o valor é todo o resto da informação.
Exemplo: {
            "123456789": {"nome": ..., "cidade": ..., "idade": ..., "zona": ...},
          ...}
• O utilizador introduz um NIF e o programa devolve o respetivo dicionário.
"""
dCli = {}
# 1. Importação e Estruturação dos Dados
try:
    with open("clientes.csv", "r", encoding="utf-8") as fp:
        # O strip() e a verificação 'if linha' evitam erros com linhas vazias no fim do arquivo
        cont = [linha.strip() for linha in fp.read().split("\n") if linha.strip()]
    for linha in cont:
        info = linha.split(";")
        nif = info[0]
        dados = info[1:] # [Nome, Cidade, Idade, Zona]
        dCli[nif] = dados
    # a) Indicar dicionário (formato inicial de lista)
    print(f"a) Dicionário importado: {dCli}")
    # b) Quantidade de registos
    print(f"\nb) Quantidade de registos lidos: {len(dCli)}")
    # c) Pessoas com idade superior a 40 anos
    maior40 = []
    for info in dCli.values():
        if int(info[2]) > 40:
            maior40.append(info[0])    
    print("\nc) Pessoas com mais de 40 anos:")
    for nome in maior40:
        print(f"\t- {nome}")
    # d) Quantidade de pessoas por zona
    zonas_lista = ["Norte", "Centro", "Sul"]
    dZonas = {zona: 0 for zona in zonas_lista} # Inicializa contadores
    
    for dados in dCli.values():
        zona = dados[3]
        if zona in dZonas:
            dZonas[zona] += 1
    print(f"\nd) Quantidade por zonas: {dZonas}")
    # e) Idade média global
    soma_total = sum(int(dados[2]) for dados in dCli.values())
    media_global = soma_total / len(dCli)
    print(f"\ne) Média de idades global: {media_global:.1f} anos")
    # f) Idade média por região
    # Criamos um dicionário onde cada chave tem sua própria lista [contador, soma]
    dZonasMedia = {zona: [0, 0] for zona in zonas_lista}

    for dados in dCli.values():
        zona = dados[3]
        idade = int(dados[2])
        if zona in dZonasMedia:
            dZonasMedia[zona][0] += 1      # Incrementa quantidade
            dZonasMedia[zona][1] += idade  # Soma idade    
    print("\nf) Média de idades por região:")

    for zona, valores in dZonasMedia.items():
        if valores[0] > 0:
            media = valores[1] / valores[0]
            print(f"\t{zona}: {media:.1f} anos")
    # g) Converter dCli para Dicionário de Dicionários
    
    for nif, info in dCli.items():
        dCli[nif] = {
            "nome": info[0],
            "cidade": info[1],
            "idade": info[2],
            "zona": info[3]
        }
    print(f"\ng) Dicionário de dicionários estruturado com sucesso.")
    # h) Consulta por NIF
    print("\nh) Consulta de Cliente")
    nifProc = input("Qual o NIF do cliente a listar? ")
    # .get() evita erro se o NIF não existir
    cliente = dCli.get(nifProc)
    
    if cliente:
        print(f"Dados do cliente {nifProc}:")

        for campo, valor in cliente.items():
            print(f"\t{campo.capitalize()}: {valor}")
    else:
        print("NIF não encontrado na base de dados.")
        
except FileNotFoundError:
    print("Erro: O arquivo 'clientes.csv' não foi encontrado.")