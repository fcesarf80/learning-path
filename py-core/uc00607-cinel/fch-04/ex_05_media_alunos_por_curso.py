"""
Exercício 05 - Media alunos por curso
Enunciado: Cria um programa que:
• Leia um ficheiro CSV (nome;curso;nota)
• Organize os alunos por curso (sugestão: dicionário de listas)
• Mostre a média de cada curso
"""
ficheiro = open("alunos.csv", "r")
cursos = {}
for linha in ficheiro:
    dados = linha.strip().split(";")
    curso = dados[1]
    nota = float(dados[2])
    
    if curso not in cursos:
        cursos[curso] = []
    cursos[curso].append(nota)
ficheiro.close()

for curso in cursos:
    soma_curso = 0
    qtd = 0
    for n in cursos[curso]:
        soma_curso += n
        qtd += 1    
    print("Média do curso", curso, ":", soma_curso / qtd)