"""
Exercicio 02 - Lista de Alunos
Enunciado: Atualize o código anterior para carregar informação de n dados de
alunos. Armazene a informação numa lista. Em seguida, apresente os valores
de cada aluno.
"""


class Aluno:
    def __init__(self, nome, sobrenome, numero, curso):
        self.nome, self.sobrenome = nome, sobrenome
        self.numero, self.curso = numero, curso

    def executar(self):
        print(
            f"Nome: {self.nome} {self.sobrenome} | "
            f"Nº: {self.numero} | Curso: {self.curso}"
        )


lista_alunos = []
quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))
for contador in range(quantidade_alunos):
    print(f"\n--- Cadastro do Aluno {contador + 1} ---")
    dados_nome = input("Digite o Nome e Sobrenome: ").split()
    nome = dados_nome[0]
    sobrenome = " ".join(dados_nome[1:])
    dados_extras = input("Digite o Nº e o Curso: ").split()
    numero = dados_extras[0]
    curso = " ".join(dados_extras[1:])
    novo_aluno = Aluno(nome, sobrenome, numero, curso)
    lista_alunos.append(novo_aluno)
print("\n--- Lista Final de Alunos ---")
for aluno in lista_alunos:
    aluno.executar()
