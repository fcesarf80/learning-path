import os
import csv
from models.livro import Livro
from models.utilizador import Utilizador

class CSVService:

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def salvar_livros(self, livros):

        with open(
            self.caminho_arquivo,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow(
                ["titulo", "autor", "ano", "categoria", "quantidade"]
            )

            for livro in livros:

                escritor.writerow([
                    livro.titulo,
                    livro.autor,
                    livro.ano,
                    livro.categoria,
                    livro.quantidade
                ])

    def carregar_livros(self):

        if not os.path.exists(self.caminho_arquivo):
            return []

        livros = []

        with open(
            self.caminho_arquivo,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.DictReader(arquivo)

            for linha in leitor:

                livro = Livro(
                    id=len(livros) + 1,
                    titulo=linha["titulo"],
                    autor=linha["autor"],
                    ano=int(linha["ano"]),
                    categoria=linha["categoria"],
                    quantidade=int(linha["quantidade"]),
                    emprestado=False,
                    data_devolucao=""
                )

                livros.append(livro)

        return livros
    
    def salvar_utilizadores(self, utilizadores):

        with open(
            self.caminho_arquivo,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow(
                ["nome", "email", "telefone"]
            )

            for utilizador in utilizadores:

                escritor.writerow([
                    utilizador.nome,
                    utilizador.email,
                    utilizador.telefone
                ])

    def carregar_utilizadores(self):

        if not os.path.exists(self.caminho_arquivo):
            return []

        utilizadores = []

        with open(
            self.caminho_arquivo,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.DictReader(arquivo)

            for linha in leitor:

                utilizador = Utilizador(
                    id=len(utilizadores) + 1,
                    nome=linha["nome"],
                    email=linha["email"],
                    telefone=linha["telefone"]
                )

                utilizadores.append(utilizador)

        return utilizadores
    
    def salvar_emprestimos(self, emprestimos):

        with open(
            self.caminho_arquivo,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            escritor = csv.writer(arquivo)

            escritor.writerow([
                "livro",
                "utilizador",
                "data_emprestimo",
                "data_prevista"
            ])

            for emprestimo in emprestimos:

                escritor.writerow([
                    emprestimo.livro,
                    emprestimo.utilizador,
                    emprestimo.data_emprestimo,
                    emprestimo.data_prevista
                ])

    def carregar_emprestimos(self):

        if not os.path.exists(self.caminho_arquivo):
            return []

        emprestimos = []

        with open(
            self.caminho_arquivo,
            mode="r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.DictReader(arquivo)

            for linha in leitor:

                emprestimos.append(linha)

        return emprestimos