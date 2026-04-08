"""
Exercício 8 – Função substituição
Enunciado: 8. Dado um tuplo, crie uma função substituir que tenha como argumentos o tuplo,
o valor que quer substituir no respetivo tuplo e ainda o valor que irá substituir.
Deve retornar o tuplo substituído. Ex: substituir(tuplo, valor_a_subs, valor_substituto)
substituir ( (1,2,3,2,3,4,1), 2, 7) ➔ (1,7,3,7,3,4,1)
"""
def substituir(tup, sai, novo):
    resp = ()  # para gerar nova tupla filtrada
    for elem in tup:
        if elem == sai:
            resp += (novo,)
        else:  # elem não é igual ao que sai, logo tem que guardar
            resp += (elem,)
    return resp
#-----------------------------
tup = (1, 2, 3, 2, 3, 4, 1)
print(f"A tupla de valores é : {tup}")
sai = int(input("Qual o valor a tirar? "))

while sai not in tup:
    sai = int(input("Qual o valor a tirar? "))

novo = int(input(f"Qual o valor a substituir {sai}?"))
resp = substituir(tup, sai, novo)
print(f"Após substituir {sai} por {novo} na tupla {tup} -> {resp}")
