"""
Exercício 05 - Media alunos por curso
Enunciado: Cria um programa que:
• Leia um ficheiro CSV (nome;curso;nota)
• Organize os alunos por curso (sugestão: dicionário de listas)
• Mostre a média de cada curso
"""
with open("alunos.csv", "w", encoding="utf-8") as f:
    f.write("Cuca;Magia;15\nSaci;Travessuras;18\nIara;Canto;20\n")
    f.write("Boto;Dança;12\nTutu;Susto;9\nCurupira;Magia;17\n")
cursos = {}
for linha in open("alunos.csv", encoding="utf-8"):
    nome, curso, nota = linha.strip().split(";")    
    if curso not in cursos:
        cursos[curso] = []
    cursos[curso].append(int(nota))
print("Médias por Curso:")
for curso, notas in cursos.items():
    media = sum(notas) / len(notas)
    print(f"Curso: {curso} | Média: {media:.1f}")
