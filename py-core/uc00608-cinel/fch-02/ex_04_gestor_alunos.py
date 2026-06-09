"""
Exercicio 04 - Gestor de Alunos Orientado a Objetos
Enunciado:Seguindo os princípios de Programação Orientada a Objetos, crie uma classe “Aluno” que contenha os atributos nome, idade e média final. Desenvolva um programa que permita gerir uma lista de alunos através de um menu com as seguintes opções:
a. Adicionar um novo aluno          d. Listar alunos ordenados pela maior média
b. Listar todos os alunos           e. Remover aluno
c. Procurar um aluno pelo nome      f. Sair do programa
"""

class Aluno:

    def __init__(self, numero, nome, sobrenome, idade, curso, media):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.numero = numero
        self.curso = curso
        self.media = media

lista_alunos = []

lista_alunos.append(
    Aluno(1, "Bart", "Simpson", 10, "4A - Edna Krabappel", 11.0)
)

lista_alunos.append(
    Aluno(2, "Milhouse", "Van Houten", 10, "4A - Edna Krabappel", 13.0)
)

lista_alunos.append(
    Aluno(3, "Nelson", "Muntz", 10, "4A - Edna Krabappel", 9.0)
)

lista_alunos.append(
    Aluno(4, "Martin", "Prince", 10, "4A - Edna Krabappel", 19.0)
)

lista_alunos.append(
    Aluno(5, "Ralph", "Wiggum", 10, "4A - Edna Krabappel", 7.0)
)

lista_alunos.append(
    Aluno(6, "Sherri", "Mackleberry", 10, "4A - Edna Krabappel", 15.0)
)

lista_alunos.append(
    Aluno(7, "Terri", "Mackleberry", 10, "4A - Edna Krabappel", 15.0)
)

lista_alunos.append(
    Aluno(8, "Wendell", "Borton", 10, "4A - Edna Krabappel", 12.0)
)

lista_alunos.append(
    Aluno(9, "Lewis", "Clark", 10, "4A - Edna Krabappel", 14.0)
)

lista_alunos.append(
    Aluno(10, "Richard", "", 10, "4A - Edna Krabappel", 13.0)
)

lista_alunos.append(
    Aluno(11, "Nina", "Skalka", 10, "4A - Edna Krabappel", 16.0)
)

lista_alunos.append(
    Aluno(12, "Sophie", "Jensen", 10, "4A - Edna Krabappel", 17.0)
)

lista_alunos.append(
    Aluno(13, "Becky", "Shorter", 10, "4A - Edna Krabappel", 14.0)
)

print("\n=== TURMA DA EDNA KRABAPPEL ===\n")

for aluno in lista_alunos:
    print(
        f"{aluno.numero:02d} - "
        f"{aluno.nome} {aluno.sobrenome}"
    )

        