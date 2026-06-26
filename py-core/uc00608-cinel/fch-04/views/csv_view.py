import tkinter as tk
from config import *

def criar_tela_csv(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA

    titulo = tk.Label(
        frame_conteudo,
        text="Importar / Exportar CSV",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )

    titulo.pack(pady=20)

    # SEÇÃO 2: BOTÕES CSV

    frame_botoes = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_botoes.pack(pady=10)

    tk.Button(
        frame_botoes,
        text="Importar Livros",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Exportar Livros",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Importar Utilizadores",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Exportar Utilizadores",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Importar Empréstimos",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    tk.Button(
        frame_botoes,
        text="Exportar Empréstimos",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    ).pack(pady=5)

    # SEÇÃO 3: INFORMAÇÕES

    tk.Label(
        frame_conteudo,
        text="Estado: Nenhuma operação realizada.",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    ).pack(pady=20)
