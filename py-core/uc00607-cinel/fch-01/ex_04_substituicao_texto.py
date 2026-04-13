"""
Exercício 4 - Substituição texto
Enunciado: Desenvolva um programa que substitua uma palavra (string) por outra
num ficheiro. As palavras e o nome do ficheiro deverão ser dados pelo utilizador.
"""
# 1. Nome do ficheiro pelo utilizador
nome_ficheiro = input("Nome do ficheiro: ")

with open(nome_ficheiro, "r", encoding="utf-8") as fp:
    cont = fp.read()

pal_velha = input("Palavra a procurar: ")
pal_nova = input("Palavra substituta: ")

# 2. Substituir
novo_cont = cont.replace(pal_velha, pal_nova)

# 3. Gravar as alterações de volta no ficheiro
with open(nome_ficheiro, "w", encoding="utf-8") as fp:
    fp.write(novo_cont)

print("Substituição concluída com sucesso!")
