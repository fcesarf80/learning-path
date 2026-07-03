import tkinter as tk
from config import *
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService

livro_service = LivroService()
utilizador_service = UtilizadorService()

csv_emprestimos = CSVService("data/emprestimos.csv")
csv_historico = CSVService("data/historico.csv")

def criar_tela_estatisticas(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(
        frame_conteudo,
        text="Estatísticas",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )
    titulo.pack(pady=20)

    tk.Label(
        frame_conteudo,
        text=f"📚 Livros: {livro_service.quantidade_livros()}",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(anchor="w", padx=30, pady=8)

    tk.Label(
        frame_conteudo,
        text=f"👤 Utilizadores: {utilizador_service.quantidade_utilizadores()}",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(anchor="w", padx=30, pady=8)

    tk.Label(
        frame_conteudo,
        text=f"📖 Empréstimos Ativos: {len(csv_emprestimos.carregar_emprestimos())}",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(anchor="w", padx=30, pady=8)

    tk.Label(
        frame_conteudo,
        text=f"📜 Histórico: {len(csv_historico.carregar_emprestimos())}",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(anchor="w", padx=30, pady=8)

    tk.Label(
        frame_conteudo,
        text=f"📦 Livros Disponíveis: {livro_service.quantidade_livros()}",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(anchor="w", padx=30, pady=8)

   
