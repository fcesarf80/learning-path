import tkinter as tk
from tkinter import ttk
from config import *

def criar_tela_devolucoes(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(
        frame_conteudo,
        text="Devolução",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = tk.Frame(
        frame_conteudo,
        bg=COR_FUNDO
    )
    frame_formulario.pack(
        padx=20,
        pady=10,
        fill="x"
    )
        
    lbl_livro = tk.Label(
        frame_formulario,
        text="Livro:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_livro.grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_livro = tk.Entry(
        frame_formulario,
        width=30,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_livro.grid(
        row=0,
        column=1,
        padx=10,
        pady=5
    )

    lbl_utilizador = tk.Label(
        frame_formulario,
        text="Utilizador:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_utilizador.grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_utilizador = tk.Entry(
        frame_formulario,
        width=30,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_utilizador.grid(
        row=1,
        column=1,
        padx=10,
        pady=5
    )

    lbl_data_devolucao = tk.Label(
        frame_formulario,
        text="Data Devolução:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_data_devolucao.grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_data_devolucao = tk.Entry(
        frame_formulario,
        width=30,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_data_devolucao.grid(
        row=2,
        column=1,
        padx=10,
        pady=5
    )

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(
        frame_conteudo,
        bg=COR_FUNDO
    )
    frame_botoes.pack(pady=10)

    btn_registar = tk.Button(
        frame_botoes,
        text="Registar Devolução",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    )
    btn_registar.pack(
        side="left",
        padx=5
    )
    
    btn_pesquisar = tk.Button(
        frame_botoes,
        text="Pesquisar",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    )
    btn_pesquisar.pack(
        side="left",
        padx=5
    )

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = tk.Frame(
        frame_conteudo,
        bg=COR_FUNDO
    )
    frame_tabela.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    colunas = (
        "livro",
        "utilizador",
        "data_emprestimo",
        "data_devolucao",
        "estado"
    )

    tabela = ttk.Treeview(
        frame_tabela,
        columns=colunas,
        show="headings"
    )

    tabela.heading(
        "livro",
        text="Livro"
    )
    tabela.heading(
        "utilizador",
        text="Utilizador"
    )
    tabela.heading(
        "data_emprestimo",
        text="Data Empréstimo"
    )
    tabela.heading(
        "data_devolucao",
        text="Data Devolução"
    )
    tabela.heading(
        "estado",
        text="Estado"
    )

    tabela.column(
        "livro",
        width=200
    )
    tabela.column(
        "utilizador",
        width=200
    )
    tabela.column(
        "data_emprestimo",
        width=150
    )
    tabela.column(
        "data_devolucao",
        width=150
    )
    tabela.column(
        "estado",
        width=120
    )
        
    tabela.pack(
        fill="both",
        expand=True
    )
