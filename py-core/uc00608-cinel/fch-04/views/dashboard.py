import tkinter as tk

from utils.background import aplicar_background

from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService


livro_service = LivroService()
utilizador_service = UtilizadorService()

csv_emprestimos = CSVService("data/emprestimos.csv")
csv_historico = CSVService("data/historico.csv")


def criar_tela_dashboard(parent):

    # Background
    aplicar_background(parent, "img/dashboard.png")

    # ===== INDICADORES =====

    lbl_livros = tk.Label(
        parent,
        text=str(livro_service.quantidade_livros()),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eaf3fe",
        bd=0,
        anchor="center"
    )

    lbl_utilizadores = tk.Label(
        parent,
        text=str(utilizador_service.quantidade_utilizadores()),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#fef6e7",
        bd=0,
        anchor="center"
    )

    lbl_emprestimos = tk.Label(
        parent,
        text=str(len(csv_emprestimos.carregar_emprestimos())),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eff6ed",
        bd=0,
        anchor="center"
    )

    lbl_historico = tk.Label(
        parent,
        text=str(len(csv_historico.carregar_emprestimos())),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eeecf9",
        bd=0,
        anchor="center"
    )
    
    lbl_livros.place(
        x=385,
        y=185,
        width=90,
        height=60
        )

    lbl_utilizadores.place(
        x=615,
        y=185,
        width=90,
        height=60
    )

    lbl_emprestimos.place(
        x=845,
        y=185,
        width=90,
        height=60
    )

    lbl_historico.place(
        x=1075,
        y=185,
        width=90,
        height=60
    )