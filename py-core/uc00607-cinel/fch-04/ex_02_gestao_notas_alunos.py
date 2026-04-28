"""
Exercício 02 - Gestão notas alunos
Enunciado: Cria um dicionário com 5 alunos e respetivas notas (entre 0 e 20) e:
• Mostra todos os alunos • Calcula a média das notas • Listagem dos alunos com nota positiva (>= 10)
"""
alunos_notas = {
    "Ana": 15, "Bruno": 8, "Carlos": 12, "Diana": 18, "Eduardo": 9
    }
soma = 0
total_alunos = 0

print("Lista de todos os alunos:")
for nome in alunos_notas:
    nota = alunos_notas[nome]
    print(nome, "-", nota)
    soma += nota
    total_alunos += 1
media = soma / total_alunos
print("\nMédia das notas:", media)

print("\nAlunos com nota positiva:")
for nome in alunos_notas:
    if alunos_notas[nome] >= 10:
        print(nome)