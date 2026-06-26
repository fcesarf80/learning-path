import tkinter as tk
from tkinter import ttk
from config import *

def criar_tela_utilizadores(frame_conteudo):

    # Configuração de fundo do frame principal da tela
    frame_conteudo.configure(bg=COR_FUNDO)

    # SEÇÃO 1: TÍTULO DA TELA
    # CORREÇÃO: Parêntese fechado e adicionada a cor de fundo
    titulo = tk.Label(frame_conteudo, text="Gestão de Utilizadores", font=FONTE_TITULO, bg=COR_FUNDO)
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_formulario.pack(padx=20, pady=10, fill="x")
        
    tk.Label(frame_formulario, text="Nome:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Email:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Telefone:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Nº Utilizador:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=3, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(frame_formulario, width=30, font=FONTE_NORMAL, highlightbackground=COR_BORDA).grid(row=3, column=1, padx=10, pady=5)

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="Adicionar", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Editar", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Remover", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Pesquisar", font=FONTE_NORMAL, bg=COR_BOTAO).pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)

    tabela = ttk.Treeview(frame_tabela, columns=("nome", "email", "telefone", "numero"), show="headings")

    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="Email")
    tabela.heading("telefone", text="Telefone")
    tabela.heading("numero", text="Nº Utilizador")

    tabela.column("nome", width=200)    
    tabela.column("email", width=250)
    tabela.column("telefone", width=150)
    tabela.column("numero", width=120)
    
    tabela.pack(fill="both", expand=True)
