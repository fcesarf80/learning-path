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

while True:

    print("\n=== GESTOR DE ALUNOS ===")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Procurar aluno")
    print("4 - Ordenar por média")
    print("5 - Remover aluno")
    print("6 - Calcular média da turma")
    print("7 - Ordenar alunos por nome")
    print("8 - Mostrar melhor aluno")
    print("9 - Mostrar pior aluno")
    print("10 - Contar alunos cadastrados")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n=== NOVO ALUNO ===")

        numero = len(lista_alunos) + 1

        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        media = float(input("Média: "))

        novo_aluno = Aluno(
            numero,
            nome,
            sobrenome,
            idade,
            curso,
            media
        )

        lista_alunos.append(novo_aluno)

        print(f"\nAluno {nome} adicionado com sucesso!")
    
    elif opcao == "2":

        print("\n=== LISTA DE ALUNOS ===\n")

        if len(lista_alunos) == 0:
            print("Nenhum aluno cadastrado.")

        else:

            for aluno in lista_alunos:

                print(
                    f"Nº: {aluno.numero} | "
                    f"Nome: {aluno.nome} {aluno.sobrenome} | "
                    f"Idade: {aluno.idade} | "
                    f"Curso: {aluno.curso} | "
                    f"Média: {aluno.media}"
                )
            
    elif opcao == "3":

        nome_procurado = input("\nNome a procurar: ")

        encontrado = False

        for aluno in lista_alunos:

            if aluno.nome.lower() == nome_procurado.lower():

                print("\n=== ALUNO ENCONTRADO ===")

                print(f"Nº: {aluno.numero}")
                print(f"Nome: {aluno.nome} {aluno.sobrenome}")
                print(f"Idade: {aluno.idade}")
                print(f"Curso: {aluno.curso}")
                print(f"Média: {aluno.media}")

                encontrado = True
                break

        if not encontrado:
            print("\nAluno não encontrado.")

    elif opcao == "4":

        print("\n=== ALUNOS ORDENADOS POR MÉDIA ===\n")

        alunos_ordenados = sorted(
            lista_alunos,
            key=lambda aluno: aluno.media,
            reverse=True
        )

        for aluno in alunos_ordenados:

            print(
                f"Nº: {aluno.numero} | "
                f"Nome: {aluno.nome} {aluno.sobrenome} | "
                f"Média: {aluno.media}"
            )

    elif opcao == "5":

        nome_remover = input("\nNome do aluno a remover: ")

        encontrado = False

        for aluno in lista_alunos:

            if aluno.nome.lower() == nome_remover.lower():

                lista_alunos.remove(aluno)

                print(f"\nAluno {aluno.nome} removido com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\nAluno não encontrado.")

    elif opcao == "6":

        if len(lista_alunos) == 0:

            print("\nNão existem alunos cadastrados.")

        else:

            soma_medias = 0

            for aluno in lista_alunos:
                soma_medias += aluno.media

            media_turma = soma_medias / len(lista_alunos)

            print("\n=== MÉDIA DA TURMA ===")
            print(f"Média geral: {media_turma:.2f}")
    
    elif opcao == "7":

        print("\n=== ALUNOS ORDENADOS POR NOME ===\n")

        alunos_ordenados = sorted(
            lista_alunos,
            key=lambda aluno: aluno.nome
        )

        for aluno in alunos_ordenados:

            print(
                f"Nº: {aluno.numero} | "
                f"{aluno.nome} {aluno.sobrenome}"
            )

    elif opcao == "8":

        if len(lista_alunos) == 0:

            print("\nNão existem alunos cadastrados.")

        else:

            melhor_aluno = max(
                lista_alunos,
                key=lambda aluno: aluno.media
            )

            print("\n=== MELHOR ALUNO ===\n")

            print(f"Nº: {melhor_aluno.numero}")
            print(f"Nome: {melhor_aluno.nome} {melhor_aluno.sobrenome}")
            print(f"Curso: {melhor_aluno.curso}")
            print(f"Média: {melhor_aluno.media}")

    elif opcao == "9":

        if len(lista_alunos) == 0:

            print("\nNão existem alunos cadastrados.")

        else:

            pior_aluno = min(
                lista_alunos,
                key=lambda aluno: aluno.media
            )

            print("\n=== PIOR ALUNO ===\n")

            print(f"Nº: {pior_aluno.numero}")
            print(f"Nome: {pior_aluno.nome} {pior_aluno.sobrenome}")
            print(f"Curso: {pior_aluno.curso}")
            print(f"Média: {pior_aluno.media}")

    elif opcao == "10":

        total_alunos = len(lista_alunos)

        print("\n=== TOTAL DE ALUNOS ===\n")
        print(f"Quantidade de alunos: {total_alunos}")
    
    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida!")



print("\n=== TURMA DA EDNA KRABAPPEL ===\n")

for aluno in lista_alunos:
    print(
        f"{aluno.numero:02d} - "
        f"{aluno.nome} {aluno.sobrenome}"
    )

        