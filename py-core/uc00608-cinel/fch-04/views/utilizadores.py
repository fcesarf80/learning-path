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

    def selecionar_utilizador(event):
        item = tabela.focus()

        if not item:
            return

        valores = tabela.item(item)["values"]

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, valores[0])

        entry_email.delete(0, tk.END)
        entry_email.insert(0, valores[1])

        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(0, valores[2])

    def editar_utilizador():
        item = tabela.focus()

        if not item:
            messagebox.showwarning(
                "Seleção",
                "Selecione um utilizador."
            )
            return

        valores = tabela.item(item)["values"]

        utilizador = utilizador_service.pesquisar_por_email(valores[1])

        if not utilizador:
            return

        utilizador.nome = entry_nome.get()
        utilizador.email = entry_email.get()
        utilizador.telefone = entry_telefone.get()

        utilizador_service.salvar_alteracoes()

        atualizar_treeview()
        limpar_campos()

    def pesquisar_utilizador():
        email = entry_email.get().strip()

        utilizador = utilizador_service.pesquisar_por_email(email)

        if not utilizador:
            messagebox.showinfo(
                "Pesquisa",
                "Utilizador não encontrado."
            )
            return

        for item in tabela.get_children():
            valores = tabela.item(item)["values"]

            if valores[1] == utilizador.email:
                tabela.selection_set(item)
                tabela.focus(item)
                tabela.see(item)
                break

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, utilizador.nome)

        entry_email.delete(0, tk.END)
        entry_email.insert(0, utilizador.email)

        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(0, utilizador.telefone)

    def remover_utilizador():
        item = tabela.focus()

        if not item:
            messagebox.showwarning(
                "Seleção",
                "Selecione um utilizador."
            )
            return

        valores = tabela.item(item)["values"]

        utilizador = utilizador_service.pesquisar_por_email(valores[1])

        if not utilizador:
            return

        utilizador_service.remover_utilizador(utilizador)

        atualizar_treeview()
        limpar_campos()

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

    btn_editar = tk.Button(
    frame_botoes,
    text="Editar",
    font=FONTE_NORMAL,
    bg=COR_BOTAO,
    command=editar_utilizador
)
    btn_editar.pack(side="left", padx=5)
    
    btn_pesquisar = tk.Button(
    frame_botoes,
    text="Pesquisar",
    font=FONTE_NORMAL,
    bg=COR_BOTAO,
    command=pesquisar_utilizador
)
    btn_pesquisar.pack(side="left", padx=5)

    btn_remover = tk.Button(
    frame_botoes,
    text="Remover",
    font=FONTE_NORMAL,
    bg=COR_BOTAO,
    command=remover_utilizador
)    
    btn_remover.pack(side="left", padx=5)

    tabela.bind("<<TreeviewSelect>>", selecionar_utilizador)
    
    atualizar_treeview()
