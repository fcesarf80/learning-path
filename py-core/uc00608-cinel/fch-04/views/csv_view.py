from tkinter import *

def criar_tela_csv(frame_conteudo):

    # SEÇÃO 1: TÍTULO DA TELA

    titulo = Label(
        frame_conteudo,
        text="Importar / Exportar CSV",
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=20)

    # SEÇÃO 2: BOTÕES CSV

    frame_botoes = Frame(frame_conteudo)
    frame_botoes.pack(pady=10)

    Button(
        frame_botoes,
        text="Importar Livros"
    ).pack(pady=5)

    Button(
        frame_botoes,
        text="Exportar Livros"
    ).pack(pady=5)

    Button(
        frame_botoes,
        text="Importar Utilizadores"
    ).pack(pady=5)

    Button(
        frame_botoes,
        text="Exportar Utilizadores"
    ).pack(pady=5)

    Button(
        frame_botoes,
        text="Importar Empréstimos"
    ).pack(pady=5)

    Button(
        frame_botoes,
        text="Exportar Empréstimos"
    ).pack(pady=5)

    # SEÇÃO 3: INFORMAÇÕES

    Label(
        frame_conteudo,
        text="Estado: Nenhuma operação realizada."
    ).pack(pady=20)