class Livro:
    def __init__(
        self,
        id: int,
        titulo: str,
        autor: str,
        ano: int,
        categoria: str,
        quantidade: int,
        emprestado: bool = False,
        data_devolucao: str = "",
    ):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.quantidade = quantidade
        self.emprestado = emprestado
        self.data_devolucao = data_devolucao

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
