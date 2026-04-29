"""
Exercício 02 - Gestão notas alunos
Enunciado: Cria um dicionário com 5 alunos e respetivas notas (entre 0 e 20) e:
• Mostra todos os alunos • Calcula a média das notas • Listagem dos alunos com nota positiva (>= 10)
"""
alunos = {"Cuca": 15, "Iara": 8, "Boto": 12, "Saci": 18, "Tutu": 9}
print("Lista de alunos e notas:\n" + "\n".join([f"{n} - {v}" for n, v in alunos.items()]))
print(f"\nMédia das notas: {sum(alunos.values()) / len(alunos)}")
positivos = [f"{n} - {v}" for n, v in alunos.items() if v >= 10]
print("\nAlunos com nota positiva (>= 10):\n" + "\n".join(positivos))