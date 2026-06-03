"""
Exercicio 05 - Agenda de Contactos Orientada a Objetos
Enunciado:Seguindo os princípios de Programação Orientada a Objetos, crie uma classe “Contacto” com vários atributos e desenvolva um programa que faça a gestão de uma agenda. O programa deve apresentar um menu com as seguintes opções:
a. Adicionar contacto       c. Procurar por nome
b. Remover contacto         d. Listar todos         e. Sair

A lista de contactos guardada em memória deve manter-se sempre ordenada de forma automática pelo "nome" do contacto.
"""

class Contato:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

contatos = []
contato = Contato("Ana","9999")
contatos.append(contato)

for contato in contatos: 

    print(contato.nome)