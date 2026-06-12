from tkinter import *

def criar_tela_estatisticas(frame_conteudo):

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = Label(frame_conteudo, text="Estatísticas", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # SEÇÃO 2: CARDS ESTATÍSTICOS
    frame_cards = Frame(frame_conteudo)
    frame_cards.pack(pady=20)

    Label(
        frame_cards,
        text="128 Livros",
        relief="solid",
        width=20,
        height=3
    ).pack(side="left", padx=10)

    Label(
        frame_cards,
        text="56 Utilizadores",
        relief="solid",
        width=20,
        height=3
    ).pack(side="left", padx=10)

    Label(
        frame_cards,
        text="18 Empréstimos",
        relief="solid",
        width=20,
        height=3
    ).pack(side="left", padx=10)

    Label(
        frame_cards,
        text="325 Histórico",
        relief="solid",
        width=20,
        height=3
    ).pack(side="left", padx=10)

    # SEÇÃO 3: RESUMO GERALLabel(
    Label(
        frame_conteudo,
        text="""
    Livros disponíveis: 110
    Livros emprestados: 18
    Utilizadores ativos: 56
    """,
        justify="left"
    ).pack(pady=20)