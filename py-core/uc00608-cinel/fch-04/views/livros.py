# IMPORTS

import tkinter as tk
from tkinter import ttk

from config import *

COR_FUNDO = "white"

FONTE_TITULO = ("Segoe UI", 20, "bold")

# FUNÇÃO PRINCIPAL

def criar_tela_livros(frame_principal):

    frame_livros = tk.Frame(
        frame_principal,
        bg=COR_FUNDO
    )

    frame_livros.pack(
        fill="both",
        expand=True
    )

    titulo = tk.Label(
        frame_livros,
        text="Gestão de Livros",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )

    titulo.pack(
        pady=20
    )

    frame_formulario = tk.Frame(
        frame_livros,
        bg=COR_FUNDO
    )

    frame_formulario.pack(
        pady=10
    )
    
    tk.Label(
        frame_formulario,
        text="Título:",
        bg=COR_FUNDO
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

    entry_titulo = tk.Entry(
        frame_formulario,
        width=40
    )

    entry_titulo.grid(
        row=0,
        column=1,
        padx=10
    )

    tk.Label(
    frame_formulario,
    text="Autor:",
    bg=COR_FUNDO
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

    entry_autor = tk.Entry(
        frame_formulario,
        width=40
    )

    entry_autor.grid(
        row=1,
        column=1,
        padx=10
    )

    tk.Label(
    frame_formulario,
    text="Categoria:",
    bg=COR_FUNDO
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

    entry_categoria = tk.Entry(
        frame_formulario,
        width=40
    )

    entry_categoria.grid(
        row=2,
        column=1,
        padx=10
    )

    tk.Label(
        frame_formulario,
        text="Quantidade:",
        bg=COR_FUNDO
    ).grid(
        row=3,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

    entry_quantidade = tk.Entry(
        frame_formulario,
        width=10
    )

    entry_quantidade.grid(
        row=3,
        column=1,
        padx=10,
        sticky="w"
    )

    frame_botoes = tk.Frame(
    frame_livros,
    bg=COR_FUNDO
    )

    frame_botoes.pack(
        pady=20
    )

# BOTÕES

    frame_botoes = tk.Frame(
        frame_livros,
        bg=COR_FUNDO
    )

    frame_botoes.pack(
        pady=20
    )

    btn_adicionar = tk.Button(
        frame_botoes,
        text="Adicionar",
        width=12
    )

    btn_adicionar.pack(
        side="left",
        padx=5
    )

    btn_editar = tk.Button(
    frame_botoes,
    text="Editar",
    width=12
    )

    btn_editar.pack(
        side="left",
        padx=5
    )

    btn_remover = tk.Button(
    frame_botoes,
    text="Remover",
    width=12
    )

    btn_remover.pack(
        side="left",
        padx=5
    )

    btn_pesquisar = tk.Button(
    frame_botoes,
    text="Pesquisar",
    width=12
)

    btn_pesquisar.pack(
        side="left",
        padx=5
    )

    colunas = (
    "titulo",
    "autor",
    "categoria",
    "quantidade"
    )

# TREEVIEW

    tree = ttk.Treeview(
    frame_livros,
    columns=colunas,
    show="headings",
    height=12
    )

    tree.heading(
    "titulo",
    text="Título"
)

    tree.heading(
        "autor",
        text="Autor"
    )

    tree.heading(
        "categoria",
        text="Categoria"
    )

    tree.heading(
        "quantidade",
        text="Quantidade"
    )

    tree.column(
    "titulo",
    width=250
    )

    tree.column(
        "autor",
        width=180
    )

    tree.column(
        "categoria",
        width=150
    )

    tree.column(
        "quantidade",
        width=100
    )

    tree.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
    )
    
    return frame_livros