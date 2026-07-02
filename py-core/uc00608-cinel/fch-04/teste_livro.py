from models.livro import Livro
from services.livro_service import LivroService

service = LivroService()

livro = Livro(
    1,
    "Frankenstein",
    "Mary Shelley",
    1818,
    "Ficção Científica",
    3
)

service.adicionar_livro(livro)

resultado = service.pesquisar_por_titulo("Frankenstein")

print(resultado)