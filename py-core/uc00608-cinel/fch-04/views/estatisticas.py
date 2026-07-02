import tkinter as tk
from config import *

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

    # SEÇÃO 2: CARDS ESTATÍSTICOS
    frame_cards = tk.Frame(
        frame_conteudo,
        bg=COR_FUNDO
    )
    frame_cards.pack(pady=20)

    # Card Livros
    card_livros = tk.Label(
        frame_cards,
        text="128 Livros",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    )
    card_livros.pack(
        side="left",
        padx=10
    )

    # Card Utilizadores
    card_utilizadores = tk.Label(
        frame_cards,
        text="56 Utilizadores",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    )
    card_utilizadores.pack(
        side="left",
        padx=10
    )

    # Card Empréstimos
    card_emprestimos = tk.Label(
        frame_cards,
        text="18 Empréstimos",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    )
    card_emprestimos.pack(
        side="left",
        padx=10
    )

    # Card Histórico
    card_historico = tk.Label(
        frame_cards,
        text="325 Histórico",
        font=FONTE_CARD,
        bg=COR_MENU,
        highlightbackground=COR_BORDA,
        highlightthickness=1,
        relief="flat",
        width=15,
        height=3
    )
    card_historico.pack(
        side="left",
        padx=10
    )

    # SEÇÃO 3: RESUMO GERAL
    texto_resumo = """
    Livros disponíveis: 110
    Livros emprestados: 18
    Utilizadores ativos: 56
    """
    
    lbl_resumo = tk.Label(
        frame_conteudo,
        text=texto_resumo,
        font=FONTE_SUBTITULO,
        bg=COR_FUNDO,
        justify="left"
    )
    lbl_resumo.pack(pady=20)
