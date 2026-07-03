from models.livro import Livro
from services.csv_service import CSVService

class LivroService:

    def __init__(self):
        self.csv_service = CSVService("data/livros.csv")
        self.livros = self.csv_service.carregar_livros()

    def adicionar_livro(self, livro: Livro):

        livro_existente = self.pesquisar_por_titulo(livro.titulo)

        if livro_existente:
            livro_existente.quantidade += livro.quantidade
        else:
            self.livros.append(livro)

        self.csv_service.salvar_livros(self.livros)

    def listar_livros(self):
        return self.livros

    def pesquisar_por_titulo(self, titulo):

        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def quantidade_livros(self):
        return len(self.livros)

    def remover_livro(self, livro):

        self.livros.remove(livro)

        self.csv_service.salvar_livros(self.livros)

    def salvar_alteracoes(self):
        self.csv_service.salvar_livros(self.livros)