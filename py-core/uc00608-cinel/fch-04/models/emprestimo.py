class Emprestimo:

    def __init__(
        self,
        livro,
        utilizador,
        data_emprestimo,
        data_prevista
    ):
        self.livro = livro
        self.utilizador = utilizador
        self.data_emprestimo = data_emprestimo
        self.data_prevista = data_prevista