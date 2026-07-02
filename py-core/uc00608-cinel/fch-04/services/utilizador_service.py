from models.utilizador import Utilizador
from services.csv_service import CSVService

class UtilizadorService:

    def __init__(self):
        self.csv_service = CSVService("data/utilizadores.csv")
        self.utilizadores = self.csv_service.carregar_utilizadores()

    def adicionar_utilizador(self, utilizador: Utilizador):
        utilizador_existente = self.pesquisar_por_email(utilizador.email)

        if utilizador_existente:
            return False

        self.utilizadores.append(utilizador)
        self.csv_service.salvar_utilizadores(self.utilizadores)
        return True

    def listar_utilizadores(self):
        return self.utilizadores

    def pesquisar_por_email(self, email):
        for utilizador in self.utilizadores:
            if utilizador.email.lower() == email.lower():
                return utilizador
        return None

    def remover_utilizador(self, utilizador):
        self.utilizadores.remove(utilizador)
        self.csv_service.salvar_utilizadores(self.utilizadores)

    def salvar_alteracoes(self):
        self.csv_service.salvar_utilizadores(self.utilizadores)
