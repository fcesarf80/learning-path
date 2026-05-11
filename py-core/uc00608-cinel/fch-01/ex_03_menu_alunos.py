"""
Exercicio 03 - Menu de Alunos e Persistência CSV
Enunciado: Seguindo a estrutura da classe “Aluno”, faça um menu com as opções:
a. Adicionar aluno, b. Remover aluno, c. Atualizar aluno, d. Sair. Quando “sair”,
o programa deverá guardar a informação num ficheiro (alunos.csv) com estrutura
csv (separador ;).
"""

import os


class Aluno:
    def __init__(self, nome, sobrenome, num, curso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.num = num
        self.curso = curso


lista_alunos = []
ARQUIVO = "alunos.csv"

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            dados = linha.strip().split(";")
            if len(dados) == 4:

                novo_aluno = Aluno(dados[0], dados[1], dados[2], dados[3])
                lista_alunos.append(novo_aluno)
    print(f"Sucesso: {len(lista_alunos)} alunos carregados do arquivo.")

while True:
    print("\n--- GESTÃO DE ALUNOS ---")
    print("a. Adicionar | b. Remover | c. Atualizar | l. Listar | d. Sair")

    opcao = input("\nEscolha uma opção: ").lower()

    if opcao == "a":
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        num = input("Nº: ")
        curso = input("Curso: ")
        lista_alunos.append(Aluno(nome, sobrenome, num, curso))
        print("Adicionado!")

    elif opcao == "b":
        num = input("Nº para remover: ")
        lista_alunos = [a for a in lista_alunos if a.num != num]
        print("Removido (se existia).")

    elif opcao == "c":
        num = input("Nº para atualizar: ")
        for a in lista_alunos:
            if a.num == num:
                a.nome = input(f"Novo Nome [{a.nome}]: ") or a.nome
                a.sobrenome = input(f"Novo Sobrenome [{a.sobrenome}]: ") or a.sobrenome
                a.curso = input(f"Novo Curso [{a.curso}]: ") or a.curso
                print("Atualizado!")
                break

    elif opcao == "l":
        print("\n--- LISTA DE ALUNOS ---")
        if not lista_alunos:
            print("A lista está vazia.")
        for a in lista_alunos:
            print(f"Nº: {a.num} | Nome: {a.nome} {a.sobrenome} | Curso: {a.curso}")

    elif opcao == "d":
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for a in lista_alunos:
                f.write(f"{a.nome};{a.sobrenome};{a.num};{a.curso}\n")
        print("Salvo com sucesso. Tchau!")
        break
