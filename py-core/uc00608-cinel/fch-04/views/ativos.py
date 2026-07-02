import tkinter as tk
from tkinter import ttk
from config import *

from services.csv_service import CSVService

csv_service = CSVService("data/emprestimos.csv")

def criar_tela_ativos(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(
        frame_conteudo,
        text="Empréstimos Ativos",
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
        "data empréstimo",
        "data prevista",
        "dias restantes"
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
        "data empréstimo",
        text="Data Empréstimo"
    )
    tabela.heading(
        "data prevista",
        text="Data Prevista"
    )
    tabela.heading(
        "dias restantes",
        text="Dias Restantes"
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
        "data empréstimo",
        width=150
    )
    tabela.column(
        "data prevista",
        width=150
    )
    tabela.column(
        "dias restantes",
        width=150
    )
        
    tabela.pack(
        fill="both",
        expand=True
    )

    def pesquisar_emprestimos():

        livro = entry_livro.get().strip().lower()
        utilizador = entry_utilizador.get().strip().lower()

        for item in tabela.get_children():
            tabela.delete(item)

        emprestimos = csv_service.carregar_emprestimos()

        for emprestimo in emprestimos:

            if (
                livro in emprestimo.livro.lower()
                and
                utilizador in emprestimo.utilizador.lower()
            ):

                tabela.insert(
                    "",
                    "end",
                    values=(
                        emprestimo.livro,
                        emprestimo.utilizador,
                        emprestimo.data_emprestimo,
                        emprestimo.data_prevista,
                        "-"
                    )
                )

    def atualizar_treeview():

        for item in tabela.get_children():
            tabela.delete(item)

        emprestimos = csv_service.carregar_emprestimos()

        for emprestimo in emprestimos:

            tabela.insert(
                "",
                "end",
                values=(
                    emprestimo.livro,
                    emprestimo.utilizador,
                    emprestimo.data_emprestimo,
                    emprestimo.data_prevista,
                    "-"
                )
            )

# SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(
        frame_conteudo,
        bg=COR_FUNDO
    )
    frame_botoes.pack(pady=10)

    btn_pesquisar = tk.Button(
    frame_botoes,
    text="Pesquisar",
    font=FONTE_NORMAL,
    bg=COR_BOTAO,
    command=pesquisar_emprestimos
    )
    btn_pesquisar.pack(
        side="left",
        padx=5
    )
        
    btn_renovar = tk.Button(
        frame_botoes,
        text="Renovar",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    )
    btn_renovar.pack(
        side="left",
        padx=5
    )
    
    btn_devolver = tk.Button(
        frame_botoes,
        text="Devolver",
        font=FONTE_NORMAL,
        bg=COR_BOTAO
    )
    btn_devolver.pack(
        side="left",
        padx=5
    )

    atualizar_treeview()

