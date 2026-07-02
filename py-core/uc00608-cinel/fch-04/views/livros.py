import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from models.livro import Livro
from services.livro_service import LivroService

livro_service = LivroService()

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

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = tk.Label(
        frame_livros,
        text="Gestão de Livros",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = tk.Frame(
        frame_livros,
        bg=COR_FUNDO
    )
    frame_formulario.pack(pady=10)
    
    # cria os Entry
    lbl_titulo = tk.Label(
        frame_formulario,
        text="Título:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_titulo.grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_titulo = tk.Entry(
        frame_formulario,
        width=40,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_titulo.grid(
        row=0,
        column=1,
        padx=10
    )

    lbl_autor = tk.Label(
        frame_formulario,
        text="Autor:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_autor.grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_autor = tk.Entry(
        frame_formulario,
        width=40,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_autor.grid(
        row=1,
        column=1,
        padx=10
    )

    lbl_categoria = tk.Label(
        frame_formulario,
        text="Categoria:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_categoria.grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_categoria = tk.Entry(
        frame_formulario,
        width=40,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_categoria.grid(
        row=2,
        column=1,
        padx=10
    )

    lbl_quantidade = tk.Label(
        frame_formulario,
        text="Quantidade:",
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_quantidade.grid(
        row=3,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )
    
    entry_quantidade = tk.Entry(
        frame_formulario,
        width=10,
        font=FONTE_NORMAL,
        highlightbackground=COR_BORDA
    )
    entry_quantidade.grid(
        row=3,
        column=1,
        padx=10,
        sticky="w"
    )

    # SEÇÃO 3: TREEVIEW
    colunas = (
        "titulo",
        "autor",
        "categoria",
        "quantidade"
    )
    
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

    # DECLARAÇÃO DAS FUNÇÕES INTERNAS (Antes do uso nos botões/binds)
    def limpar_campos():
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)

    def adicionar_livro():
        if entry_titulo.get().strip() == "":
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o título do livro."
            )
            return

        if entry_autor.get().strip() == "":
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o autor."
            )
            return

        if entry_categoria.get().strip() == "":
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe a categoria."
            )
            return

        if entry_quantidade.get().strip() == "":
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe a quantidade."
            )
            return
            
        # Validação do número inteiro feita antes de construir o objeto
        try:
            quantidade_validada = int(entry_quantidade.get())
        except ValueError:
            messagebox.showwarning(
                "Quantidade inválida",
                "A quantidade deve ser um número inteiro."
            )
            return

        livro = Livro(
            id=len(livro_service.livros) + 1,
            titulo=entry_titulo.get(),
            autor=entry_autor.get(),
            ano=2026,
            categoria=entry_categoria.get(),
            quantidade=quantidade_validada,
            emprestado=False,
            data_devolucao=""
        )
        livro_service.adicionar_livro(livro)

        atualizar_treeview()
        
        limpar_campos()
     
    def editar_livro():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Seleção vazia", "Selecione um livro na tabela para editar.")
            return
            
        dados = tree.item(item)
        valores = dados["values"]

        livro = livro_service.pesquisar_por_titulo(valores[0])

        try:
            quantidade_validada = int(entry_quantidade.get())
        except ValueError:
            messagebox.showwarning(
                "Quantidade inválida",
                "A quantidade deve ser um número inteiro."
            )
            return

        livro.titulo = entry_titulo.get()
        livro.autor = entry_autor.get()
        livro.categoria = entry_categoria.get()
        livro.quantidade = quantidade_validada
        livro_service.salvar_alteracoes()
        
        tree.item(
            item,
            values=(
                entry_titulo.get(),
                entry_autor.get(),
                entry_categoria.get(),
                entry_quantidade.get()
            )
        )
        limpar_campos()        

    def selecionar_livro(event):
        item = tree.focus()
        if not item:
            return
        
        dados = tree.item(item)
        valores = dados["values"]

        if len(valores) < 4:
            return
   
        entry_titulo.delete(0, tk.END)
        entry_titulo.insert(0, valores[0])

        entry_autor.delete(0, tk.END)
        entry_autor.insert(0, valores[1])

        entry_categoria.delete(0, tk.END)
        entry_categoria.insert(0, valores[2])

        entry_quantidade.delete(0, tk.END)
        entry_quantidade.insert(0, valores[3])

    def remover_livro():
        item = tree.focus()
        if not item:
            messagebox.showwarning("Seleção vazia", "Selecione um livro na tabela para remover.")
            return

        dados = tree.item(item)
        valores = dados["values"]

        livro = livro_service.pesquisar_por_titulo(valores[0])
        livro_service.remover_livro(livro)
       
        tree.delete(item)
        limpar_campos()

    def atualizar_treeview():
        for item in tree.get_children():
            tree.delete(item)

        for livro in livro_service.listar_livros():
            tree.insert(
                "",
                "end",
                values=(
                    livro.titulo,
                    livro.autor,
                    livro.categoria,
                    livro.quantidade
                )
            )

    def pesquisar_livro():
        titulo = entry_titulo.get()
       
        livro = livro_service.pesquisar_por_titulo(titulo)
       
        if not livro:
            messagebox.showinfo("Busca", "Nenhum livro encontrado com este título.")
            return
        
        for item in tree.get_children():
            valores = tree.item(item)["values"]
            if valores[0] == livro.titulo:
                tree.selection_set(item)
                tree.focus(item)
                tree.see(item)
                break

        entry_titulo.delete(0, tk.END)
        entry_titulo.insert(0, livro.titulo)

        entry_autor.delete(0, tk.END)
        entry_autor.insert(0, livro.autor)

        entry_categoria.delete(0, tk.END)
        entry_categoria.insert(0, livro.categoria)

        entry_quantidade.delete(0, tk.END)
        entry_quantidade.insert(0, livro.quantidade)

    # Vinculando o evento da Treeview
    tree.bind("<<TreeviewSelect>>", selecionar_livro)

    # SEÇÃO 4: BOTÕES DE AÇÃO
    frame_botoes = tk.Frame(
        frame_livros,
        bg=COR_FUNDO
    )
    frame_botoes.pack(pady=20)

    btn_adicionar = tk.Button(
        frame_botoes,
        text="Adicionar",
        width=12,
        font=FONTE_NORMAL,
        bg=COR_BOTAO,
        command=adicionar_livro
    )
    btn_adicionar.pack(side="left", padx=5)

    btn_editar = tk.Button(
        frame_botoes,
        text="Editar",
        width=12,
        font=FONTE_NORMAL,
        bg=COR_BOTAO,
        command=editar_livro
    )
    btn_editar.pack(side="left", padx=5)

    btn_remover = tk.Button(
        frame_botoes,
        text="Remover",
        width=12,
        font=FONTE_NORMAL,
        bg=COR_BOTAO,
        command=remover_livro
    )
    btn_remover.pack(side="left", padx=5)

    btn_pesquisar = tk.Button(
        frame_botoes,
        text="Pesquisar",
        width=12,
        font=FONTE_NORMAL,
        bg=COR_BOTAO,
        command=pesquisar_livro
    )
    btn_pesquisar.pack(
        side="left",
        padx=5
    )

    atualizar_treeview()
