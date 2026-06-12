from tkinter import *
from tkinter import ttk

def criar_tela_utilizadores(frame_conteudo):

    # SEÇÃO 1: TÍTULO DA TELA
    titulo = Label(frame_conteudo, text="Gestão de Utilizadores", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # SEÇÃO 2: FORMULÁRIO DE DADOS
    frame_formulario = Frame(frame_conteudo)
    frame_formulario.pack(padx=20, pady=10, fill="x")
        
    Label(frame_formulario, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=0, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=1, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Telefone:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=2, column=1, padx=10, pady=5)

    Label(frame_formulario, text="Nº Utilizador:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Entry(frame_formulario, width=30).grid(row=3, column=1, padx=10, pady=5)

    # SEÇÃO 3: BOTÕES DE AÇÃO
    frame_botoes = Frame(frame_conteudo)
    frame_botoes.pack(pady=10)

    Button(frame_botoes, text="Adicionar").pack(side="left", padx=5)
    Button(frame_botoes, text="Editar").pack(side="left", padx=5)
    Button(frame_botoes, text="Remover").pack(side="left", padx=5)
    Button(frame_botoes, text="Pesquisar").pack(side="left", padx=5)

    # SEÇÃO 4: TABELA DE REGISTROS (TREEVIEW)
    frame_tabela = Frame(frame_conteudo)
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