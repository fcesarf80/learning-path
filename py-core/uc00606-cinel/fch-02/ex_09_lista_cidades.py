"""
Exercício 9 – Lista cidades input
Enunciado: 9. Pretende-se guardar numa lista o nome de 5 cidades que serão solicitadas ao utilizador.
"""

cidades = [] #armazenar os nomes lidos
for x in  range(1,6):
    cidades.append(input(f"Qual o nome da {x}º cidade a guardar? "))

print(f"As cidades são: {'\n'.join(cidades)}")
