import tkinter as tk
from tkinter import ttk
from config import *

def criar_tela_ativos(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(frame_conteudo, text="Empréstimos Ativos", font=FONTE_TITULO, bg=COR_FUNDO)
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_formulario.pack(padx=20, pady=10, fill="x")
        
    tk.Label(frame_formulario, text="Livro:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Utilizador:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=1, column=1, padx=10, pady=5)

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="Pesquisar", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Renovar", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Devolver", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    tabela = ttk.Treeview(frame_tabela, columns=("livro", "utilizador", "data empréstimo", "data prevista", "dias restantes"), show="headings")

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
