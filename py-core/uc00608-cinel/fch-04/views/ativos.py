import tkinter as tk
from tkinter import ttk

def criar_tela_ativos(frame_conteudo):

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = Label(frame_conteudo, text="Empréstimos Ativos", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = Frame(frame_conteudo)
    frame_formulario.pack(padx=20, pady=10, fill="x")
        
    Label(frame_formulario, text="Livro:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=0, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Utilizador:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=1, column=1, padx=10, pady=5)

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = Frame(frame_conteudo)
    frame_botoes.pack(pady=10)

    Button(frame_botoes, text="Pesquisar").pack(side="left", padx=5)
    Button(frame_botoes, text="Renovar").pack(side="left", padx=5)
    Button(frame_botoes, text="Devolver").pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = Frame(frame_conteudo)
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    tabela = ttk.Treeview(frame_tabela, columns=("nome", "email", "telefone", "numero"), show="headings")

    tabela.heading("livro", text="Livro")
    tabela.heading("utilizador", text="Utilizador")
    tabela.heading("data empréstimo", text="Data Empréstimo")
    tabela.heading("data prevista", text="Data Prevista")
    tabela.heading("dias restantes", text="Dias Restantes")

    tabela.column("livro", width=200)    
    tabela.column("utilizador", width=200)
    tabela.column("data empréstimo", width=150)
    tabela.column("data prevista", width=150)
    tabela.column("dias restantes", width=150)
        
    tabela.pack(fill="both", expand=True)