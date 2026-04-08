"""
Exercício 11 – Remocao segura lista
Enunciado: 11. Utilizando a lista de nomes de cidades da alínea anterior, solicite ao utilizador um nome dessas cidades
e o remova da lista. Caso não seja possível realizar a remoção da cidade, essa informação deverá ser dada ao utilizador.
"""

cid = ["Porto", "Braga", "Faro","Viseu", "Lisboa"]
print(cid)

sai = input("Qual a cidade a remover? ")
while sai not in cid:
    print(f"A cidade {sai} não faz parte da lista")
    print(f"A lista de cidades é: {cid}")
    sai = input("Qual a cidade a remover? ")
pos = cid.index(sai)
del(cid[pos])
print(f"Após remover {sai} a lista fica: {cid}")
