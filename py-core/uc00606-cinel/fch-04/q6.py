"""
6) Considere a seguinte lista de elementos, onde cada elemento é uma tupla com o nome da pessoa e o segundo elemento a cidade onde vive: [('Ana', 'Braga'), ('Zé', 'Faro'), ('Nelo', 'Braga'), ('Xica', 'Beja'), ('Pedro', 'Covilhães')]. Dado o nome de uma pessoa, mostrar onde ela vive e todas as ocorrências do nome dado. Qual a cidade com mais habitantes registados na lista? E dado o nome de uma pessoa, remover a tupla referente a essa pessoa da lista e apresentar a lista ao utilizador.

"""
pes = [("Ana", "Braga"), ("Zé", "Faro"),("Nelo", "Braga"),
           ("Xica", "Beja"), ("Pedro", "Covilhã")]
nome = input("Nome da pessoa: ")
for item in pes:
    if item[0] == nome:
        print(nome, "vive em", item[1])
cdds = []
for item in pes:
    cdds.append(item[1])
cdd = max(set(cdds), key=cdds.count)
print("Cidade com mais habitantes registrados:", cdd)
pes = [item for item in pes if item[0] != nome]
print("Lista atualizada")
print(pes)