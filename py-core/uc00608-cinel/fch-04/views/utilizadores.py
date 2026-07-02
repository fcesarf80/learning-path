import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from config import *
from models.utilizador import Utilizador
from services.utilizador_service import UtilizadorService

utilizador_service = UtilizadorService()


def criar_tela_utilizadores(frame_conteudo):

    frame_utilizadores = tk.Frame(frame_conteudo, bg=COR_FUNDO)
    frame_utilizadores.pack(fill="both", expand=True)

    titulo = tk.Label(
        frame_utilizadores, text="Gestão de Utilizadores", font=FONTE_TITULO, bg=COR_FUNDO
    )
    titulo.pack(pady=20)

    frame_formulario = tk.Frame(frame_utilizadores, bg=COR_FUNDO)
    frame_formulario.pack(pady=10)

    lbl_nome = tk.Label(
        frame_formulario, text="Nome:", font=FONTE_NORMAL, bg=COR_FUNDO
    )
    lbl_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry_nome = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL)
    entry_nome.grid(row=0, column=1, padx=10)

    lbl_email = tk.Label(
        frame_formulario, text="Email:", font=FONTE_NORMAL, bg=COR_FUNDO
    )
    lbl_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    entry_email = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL)
    entry_email.grid(row=1, column=1, padx=10)

    lbl_telefone = tk.Label(
        frame_formulario, text="Telefone:", font=FONTE_NORMAL, bg=COR_FUNDO
    )
    lbl_telefone.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    entry_telefone = tk.Entry(frame_formulario, width=40, font=FONTE_NORMAL)
    entry_telefone.grid(row=2, column=1, padx=10)

    # TREEVIEW
    colunas = ("nome", "email", "telefone")

    tabela = ttk.Treeview(
        frame_utilizadores, columns=colunas, show="headings", height=12
    )

    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="Email")
    tabela.heading("telefone", text="Telefone")

    tabela.column("nome", width=250)
    tabela.column("email", width=250)
    tabela.column("telefone", width=180)

    tabela.pack(fill="both", expand=True, padx=20, pady=20)

    def adicionar_utilizador():
        utilizador = Utilizador(
            id=len(utilizador_service.utilizadores) + 1,
            nome=entry_nome.get(),
            email=entry_email.get(),
            telefone=entry_telefone.get()
        )

        if utilizador_service.adicionar_utilizador(utilizador):
            atualizar_treeview()
            limpar_campos()
        else:
            messagebox.showwarning(
                "Utilizador existente",
                "Já existe um utilizador com este e-mail."
            )

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)

    def atualizar_treeview():
        for item in tabela.get_children():
            tabela.delete(item)

        for utilizador in utilizador_service.listar_utilizadores():
            tabela.insert(
                "",
                "end",
                values=(
                    utilizador.nome,
                    utilizador.email,
                    utilizador.telefone
                )
            )

    frame_botoes = tk.Frame(frame_utilizadores, bg=COR_FUNDO)
    frame_botoes.pack(pady=10)

    btn_adicionar = tk.Button(
        frame_botoes,
        text="Adicionar",
        font=FONTE_NORMAL,
        bg=COR_BOTAO,
        command=adicionar_utilizador
    )
    btn_adicionar.pack(side="left", padx=5)

    # Carrega os dados iniciais na tabela ao abrir a tela
    atualizar_treeview()
