"""
Exercicio 04 - Gestor de Alunos Orientado a Objetos
Enunciado:Seguindo os princípios de Programação Orientada a Objetos, crie uma classe “Aluno” que contenha os atributos nome, idade e média final. Desenvolva um programa que permita gerir uma lista de alunos através de um menu com as seguintes opções:
a. Adicionar um novo aluno          d. Listar alunos ordenados pela maior média
b. Listar todos os alunos           e. Remover aluno
c. Procurar um aluno pelo nome      f. Sair do programa
"""
class Aluno:

    def __init__(self, numero, nome, sobrenome, idade, curso, media):
        self.nome, self.sobrenome = nome, sobrenome
        self.idade, self.numero = idade, numero
        self.curso, self.media = curso, media
    
print("Programa iniciado")
        