import tkinter as tk
from config import *

def criar_tela_estatisticas(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(frame_conteudo, text="Estatísticas", font=FONTE_TITULO, bg=COR_FUNDO)
    titulo.pack(pady=20)

    # SEÇÃO 2: CARDS ESTATÍSTICOS
    frame_cards = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_cards.pack(pady=20)

    # Cards configurados com a COR_MENU no fundo, contorno discreto com COR_BORDA e FONTE_CARD
    tk.Label(
        frame_cards,
        text="128 Livros",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    ).pack(side="left", padx=10)

    tk.Label(
        frame_cards,
        text="56 Utilizadores",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    ).pack(side="left", padx=10)

    tk.Label(
        frame_cards,
        text="18 Empréstimos",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    ).pack(side="left", padx=10)

    tk.Label(
        frame_cards,
        text="325 Histórico",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    ).pack(side="left", padx=10)

    # SEÇÃO 3: RESUMO GERAL
    tk.Label(
        frame_conteudo,
        text="""
    Livros disponíveis: 110
    Livros emprestados: 18
    Utilizadores ativos: 56
    """,
        font=FONTE_SUBTITULO,
        bg=COR_FUNDO,
        justify="left"
    ).pack(pady=20)
