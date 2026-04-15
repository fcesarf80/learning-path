"""
Exercício 03 - Gestão NIF
Enunciado:Considere o seguinte arquivo csv coma seguinte estrutura:
123456789;Ana;Lisboa;22;Centro - 987654321;Pedro;Porto;45;Norte
192837465;Isabel;Coimbra;22;Centro - 564738291;Ana;Chaves;33;Norte
837465192;José;Beja;45;Sul - 748392615;Francisco;Bragança;19;Norte
615294837;Pedro;Faro;23;Sul - 294837156;José;Covilhã;56;Centro
483920176;Marta;Bragança;28;Norte - 572940183;Luís;Aveiro;39;Centro
620481739;Carla;Setúbal;31;Sul - 918273645;Rui;Évora;47;Sul
736291840;Sofia;Viseu;26;Centro - 840192736;Bruno;Guimarães;34;Norte
369258147;Helena;Évora;52;Sul - 501928374;Tiago;Coimbra;29;Centro
210394857;Patrícia;Bragança;41;Norte - 475839102;André;Santarém;38;Centro
Importe o conteúdo do arquivo para um dicionário onde a chave será o 1º campo (NIF).
Os restantes elementos de cada linha deverão ser armazenados como lista associados à chave NIF.
• Deverá indicar quantos registos foram lidos do arquivo,
• Apresente os nomes de todas as pessoas com idade superior a 40 anos,
• Construir um dicionário onde possa valvar a informação de quantas pessoas
existem por zona do país (exemplo: {"Norte": X, "Centro": Y, "Sul": Z})
• Calcule a idade média dos contatos.
• Construa um novo dicionário com a idade média por região
(ex: {"Norte": média1, "Centro": média2, "Sul": média3}
• Criar um dicionário onde a chave é o NIF e o valor é todo o resto da informação.
Exemplo: {
            "123456789": {"nome": ..., "cidade": ..., "idade": ..., "zona": ...},
          ...}
• O utilizador introduz um NIF e o programa devolve o respectivo dicionário.
"""
import os

diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_script, "clientes.csv")

dCli = {}

try:
    
    with open(caminho_csv, "r", encoding="utf-8") as fp:
        # Filtra linhas vazias para evitar erros no split
        cont = [linha.strip() for linha in fp.read().split("\n") if linha.strip()]

    for linha in cont:
        info = linha.split(";")
        nif = info[0]
        dados = info[1:]  
        dCli[nif] = dados

    print(f"a) Dicionário importado com sucesso.")
    print(f"b) Quantidade de registos lidos: {len(dCli)}")
    # c) Pessoas com idade superior a 40 anos
    maior40 = [info[0] for info in dCli.values() if int(info[2]) > 40]
    print("\nc) Nomes com mais de 40 anos:")
    for nome in maior40:
        print(f"\t- {nome}")
    # d) Quantidade de pessoas por zona
    zonas_ref = ["Norte", "Centro", "Sul"]
    dZonas = {zona: 0 for zona in zonas_ref}
    for dados in dCli.values():
        zona = dados[3]
        if zona in dZonas:
            dZonas[zona] += 1
    print(f"\nd) Quantidade por zonas: {dZonas}")
    # e) Média de idades global
    soma_idades = sum(int(dados[2]) for dados in dCli.values())
    print(f"\ne) Média de idades global: {soma_idades/len(dCli):.1f} anos")
    # f) Média de idades por zona  
    dZonasMedia = {zona: [0, 0] for zona in zonas_ref} 
    for dados in dCli.values():
        zona = dados[3]
        idade = int(dados[2])
        if zona in dZonasMedia:
            dZonasMedia[zona][0] += 1
            dZonasMedia[zona][1] += idade
    print("\nf) Média de idades por zona:")
    for zona, valores in dZonasMedia.items():
        if valores[0] > 0:
            media = valores[1] / valores[0]
            print(f"\t{zona}: {media:.1f} anos")
    # g) Criar dicionário de dicionários (Estrutura final)
    for nif, info in dCli.items():
        dCli[nif] = {
            "nome": info[0],
            "cidade": info[1],
            "idade": info[2],
            "zona": info[3]
        }
    print("\ng) Dicionário de dicionários estruturado.")
    # h) Busca por NIF
    print("\nh) Consulta de Cliente")
    nif_proc = input("Qual o NIF do cliente a listar? ")
    cliente = dCli.get(nif_proc)

    if cliente:
        print(f"Dados do cliente {nif_proc}:")
        for campo, valor in cliente.items():
            print(f"\t{campo.capitalize()}: {valor}")
    else:
        print("Aviso: NIF não encontrado.")

except FileNotFoundError:
    print(f"Erro: O arquivo 'clientes.csv' não foi encontrado em: {caminho_csv}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")