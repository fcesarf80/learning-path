"""
Exercício 10 – Troca cidades validacao
Enunciado: 10. Numa lista de nomes de cidades (definida por si), troque o nome de uma cidade por outra, cidades essas 
solicitadas ao utilizador. Deverá fazer a validação de que a cidade que deseja substituir existe na lista.
"""

cid = ["Porto", "Braga", "Faro","Viseu", "Porto"]
print(cid)
sai = ""
while sai not in cid:
    sai = input("Qual a cidade você quer substituir? ")

nova = input(f"Qual a cidade a substituir {sai}? ")

for i, nome in enumerate(cid):
    if nome == sai:
        cid[i] = nova
        break
print(cid)
