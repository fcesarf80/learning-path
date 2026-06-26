import tkinter as tk
from tkinter import ttk

def criar_tela_devolucoes(frame_conteudo):

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = Label(frame_conteudo, text="Devolução", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = Frame(frame_conteudo)
    frame_formulario.pack(padx=20, pady=10, fill="x")
        
    Label(frame_formulario, text="Livro:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=0, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Utilizador:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=1, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Data Devolução:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=1, column=1, padx=10, pady=5)

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = Frame(frame_conteudo)
    frame_botoes.pack(pady=10)

    Button(frame_botoes, text="Registar Devolução").pack(side="left", padx=5)
    Button(frame_botoes, text="Pesquisar").pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = Frame(frame_conteudo)
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    tabela = ttk.Treeview(frame_tabela, columns=("livro", "utilizador", "data_emprestimo", "data_devolucao", "estado"), show="headings")

    tabela.heading("livro", text="Livro")
    tabela.heading("utilizador", text="Utilizador")
    tabela.heading("data_emprestimo", text="Data Empréstimo")
    tabela.heading("data_devolucao", text="Data Devolução")
    tabela.heading("estado", text="Estado")

    tabela.column("livro", width=200)
    tabela.column("utilizador", width=200)
    tabela.column("data_emprestimo", width=150)
    tabela.column("data_devolucao", width=150)
    tabela.column("estado", width=120)
        
    tabela.pack(fill="both", expand=True)