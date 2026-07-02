from models.emprestimo import Emprestimo


class EmprestimoService:

    def __init__(self):
        self.emprestimos = []

    def realizar_emprestimo(self, livro, utilizador):

        if livro.quantidade <= 0:
            return False

        livro.quantidade -= 1

        emprestimo = Emprestimo(
            livro,
            utilizador
        )

        self.emprestimos.append(emprestimo)

        return True

    def listar_emprestimos(self):
        return self.emprestimos