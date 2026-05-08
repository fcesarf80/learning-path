"""
Exercicio 03 - Menu de Alunos e Persistência CSV
Enunciado: Seguindo a estrutura da classe “Aluno”, faça um menu com as opções:
a. Adicionar aluno, b. Remover aluno, c. Atualizar aluno, d. Sair. Quando “sair”,
o programa deverá guardar a informação num ficheiro (alunos.csv) com estrutura 
csv (separador ;).
"""
class Aluno:
    def __init__(self, nome, sobrenome, num, curso):
        self.nome, self.sobrenome = nome, sobrenome
        self.num, self.curso = num, self.curso

#######################
def adicionar():
    nome = input("Qual o nome do aluno?")
    sobrenome = input("Qual o sobrenome do aluno {nome}? ")

    num = input(f"Qual o nº do aluno {nome} {sobrenome} na turma? ")
    while True:
        print("\n\n\n\n")
        print("a) Adicional aluno")
        print("b) Remover aluno")
        print("c) Atualizar aluno")
        print("d) Mostrar dados de todos")
        print("e) Sair")

        op = input("Escolha a sua opção: ").lower()
        match op:
            case "a":
                adicionar()
            case "b":
                remover()
            case "c":
                atualizar()
            case "d":
                mostrar()
            case "e":
                sair()
                break
            case _:
                sair()
                print("Opção invalida")
                print("")

turma = [aluno_01, aluno_02,...]
for aluno in turma:
    if numero == aluno.num: