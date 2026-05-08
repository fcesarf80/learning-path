"""
Exercicio 03 - Menu de Alunos e Persistência CSV
Enunciado: Seguindo a estrutura da classe “Aluno”, faça um menu com as opções:
a. Adicionar aluno, b. Remover aluno, c. Atualizar aluno, d. Sair. Quando “sair”,
o programa deverá guardar a informação num ficheiro (alunos.csv) com estrutura 
csv (separador ;).
"""
class Aluno:
    def __init__(self,nome sobrenome,num,curso):
        self.nome, self.sobrenome = nome, sobrenome
        self.num, self.curso = num, self.curso

#######################
while True:
    print("a) Adicionar aluno")
    print("b) Remover aluno")
    print("c) Atualizar aluno")
    print("d) Mostrar dados de todos")
    print("e) Sair")

    op = input("Escolha a sua opção: ")

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
            
        