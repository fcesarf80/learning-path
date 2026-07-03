from models.emprestimo import Emprestimo
from services.csv_service import CSVService

class EmprestimoService:

    def __init__(self):
        self.csv_service = CSVService(
            "data/emprestimos.csv"
        )
        self.emprestimos = self.csv_service.carregar_emprestimos()

    def realizar_emprestimo(
        self,
        livro,
        utilizador,
        data_emprestimo,
        data_prevista
    ):

        if livro.quantidade <= 0:
            return False

        livro.quantidade -= 1

        emprestimo = Emprestimo(
            livro.titulo,
            utilizador.nome,
            data_emprestimo,
            data_prevista
        )

        self.emprestimos.append(
            emprestimo
        )

        self.csv_service.salvar_emprestimos(
            self.emprestimos
        )

        return True

    def listar_emprestimos(self):
        return self.emprestimos
    
    def remover_emprestimo(
        self, 
        livro, 
        utilizador
    ):

        self.emprestimos = [
            e for e in self.emprestimos
            if not (
                e.livro == livro and
                e.utilizador == utilizador
            )
        ]

        self.csv_service.salvar_emprestimos(
            self.emprestimos
        )
