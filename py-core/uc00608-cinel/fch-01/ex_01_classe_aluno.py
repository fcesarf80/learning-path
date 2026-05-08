"""
Exercicio 01 - Classe Aluno
Enunciado: Desenvolva a classe Aluno com as propriedades nome,
sobrenome, número e curso, e um método para a visualização dos dados.
"""
class Aluno:
    def __init__(self, nome, sobrenome, numero, curso):
        self.nome, self.sobrenome = nome, sobrenome
        self.numero, self.curso = numero, curso
    def exibir_dados(self):
        print(f"Nome: {self.nome} {self.sobrenome} | "
              f"Nº: {self.numero} | Curso: {self.curso}")
aluno1 = Aluno("Pato", "Donald", 313, "Marujo")
aluno1.exibir_dados()