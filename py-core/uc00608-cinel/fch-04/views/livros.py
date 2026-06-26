import tkinter as tk
from tkinter import ttk
from config import *

# FUNÇÃO PRINCIPAL
def criar_tela_livros(frame_principal):

    frame_livros = tk.Frame(frame_principal, bg=COR_FUNDO)
    frame_livros.pack(fill="both", expand=True)

    # SEÇÃO 1: TÍTULO DA TELA
    # Alterado para usar FONTE_TITULO do config.py
    titulo = tk.Label(frame_livros, text="Gestão de Livros", font=FONTE_TITULO, bg=COR_FUNDO)
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = tk.Frame(frame_livros, bg=COR_FUNDO)
    frame_formulario.pack(pady=10)
    
    # Aplicada a FONTE_NORMAL e contorno com COR_BORDA nos campos de entrada
    tk.Label(frame_formulario, text="Título:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_titulo = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL, highlightbackground=COR_BORDA)
    entry_titulo.grid(row=0, column=1, padx=10)

    tk.Label(frame_formulario, text="Autor:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_autor = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL, highlightbackground=COR_BORDA)
    entry_autor.grid(row=1, column=1, padx=10)

    tk.Label(frame_formulario, text="Categoria:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_categoria = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL, highlightbackground=COR_BORDA)
    entry_categoria.grid(row=2, column=1, padx=10)

    tk.Label(frame_formulario, text="Quantidade:", font=FONTE_NORMAL, bg=COR_FUNDO).grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_quantidade = tk.Entry(frame_formulario, width=10, font=FONTE_NORMAL, highlightbackground=COR_BORDA)
    entry_quantidade.grid(row=3, column=1, padx=10, sticky="w")

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(frame_livros, bg=COR_FUNDO)
    frame_botoes.pack(pady=20)

    # Aplicada a COR_BOTAO e FONTE_NORMAL do arquivo de configuração
    btn_adicionar = tk.Button(frame_botoes, text="Adicionar", width=12, font=FONTE_NORMAL, bg=COR_BOTAO)
    btn_adicionar.pack(side="left", padx=5)

    btn_editar = tk.Button(frame_botoes, text="Editar", width=12, font=FONTE_NORMAL, bg=COR_BOTAO)
    btn_editar.pack(side="left", padx=5)

    btn_remover = tk.Button(frame_botoes, text="Remover", width=12, font=FONTE_NORMAL, bg=COR_BOTAO)
    btn_remover.pack(side="left", padx=5)

    btn_pesquisar = tk.Button(frame_botoes, text="Pesquisar", width=12, font=FONTE_NORMAL, bg=COR_BOTAO)
    btn_pesquisar.pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    colunas = ("titulo", "autor", "categoria", "quantidade")
    
    tree = ttk.Treeview(frame_livros, columns=colunas, show="headings", height=12)

    tree.heading("titulo", text="Título")
    tree.heading("autor", text="Autor")
    tree.heading("categoria", text="Categoria")
    tree.heading("quantidade", text="Quantidade")

    tree.column("titulo", width=250)
    tree.column("autor", width=180)
    tree.column("categoria", width=150)
    tree.column("quantidade", width=100)

    tree.pack(fill="both", expand=True, padx=20, pady=20)
    
    return frame_livros
