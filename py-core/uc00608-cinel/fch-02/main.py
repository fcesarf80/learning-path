# ==================================================
# IMPORTS
# ==================================================

import tkinter as tk

from tkinter import filedialog
from pathlib import Path
from PIL import Image
from PIL import ImageTk
from services.gestor_alunos import lista_alunos

# ==================================================
# CONFIGURAÇÕES E VARIÁVEIS GLOBAIS
# ==================================================

aluno_atual = lista_alunos[0]
indice_aluno = 0

# ==================================================
# FUNÇÕES DA INTERFACE
# ==================================================

def carregar_foto():

    caminho_foto = filedialog.askopenfilename(
        title="Selecionar foto do aluno",
        filetypes=[
            ("Imagens PNG", "*.png"),
            ("Todos os ficheiros", "*.*")
        ]
    )

    if caminho_foto:

        imagem = Image.open(caminho_foto)

        nova_foto = ImageTk.PhotoImage(imagem)

        label_foto.config(
            image=nova_foto
        )

        label_foto.image = nova_foto

def proximo_aluno():

    global indice_aluno

    if indice_aluno < len(lista_alunos) - 1:

        indice_aluno += 1

        mostrar_aluno()

def aluno_anterior():

    global indice_aluno

    if indice_aluno > 0:

        indice_aluno -= 1

        mostrar_aluno()

        
def mostrar_aluno():

    global foto_aluno

    # OBTÉM O ALUNO ATUAL

    aluno = lista_alunos[indice_aluno]

    # MONTA O CAMINHO DA FOTO

    caminho_foto = (
        BASE_DIR
        / "img"
        / "class-edna-krabappel"
        / aluno.foto
    )

    # ATUALIZA OS DADOS TEXTUAIS

    nome_completo = (
        f"{aluno.nome} {aluno.sobrenome}"
    )

    label_nome.config(
        text=nome_completo
    )

    label_numero.config(
        text=f"Nº: {aluno.numero}"
    )

    label_idade.config(
    text=f"Idade: {aluno.idade}"
    )

    label_curso.config(
    text=f"Curso: {aluno.curso}"
    )

    label_media.config(
    text=f"Média: {aluno.media}"
    )    

    # ATUALIZA A FOTO

    imagem = Image.open(caminho_foto)

    foto_aluno = ImageTk.PhotoImage(imagem)

    label_foto.config(
        image=foto_aluno
    )
    
    label_foto.image = foto_aluno

# ==================================================
# JANELA PRINCIPAL
# ==================================================

janela = tk.Tk()

janela.title("Gestor de Alunos - Turma da Edna")
janela.geometry("1366x768")
janela.resizable(False, False)

# ==================================================
# BACKGROUND
# ==================================================

BASE_DIR = Path(__file__).parent

caminho_fundo = BASE_DIR / "img" / "tela" / "background.png"

imagem_fundo = Image.open(caminho_fundo)

imagem_fundo = imagem_fundo.resize(
    (1112, 743)
)

fundo = ImageTk.PhotoImage(imagem_fundo)

label_fundo = tk.Label(
    janela,
    image=fundo
)

label_fundo.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

# ==================================================
# FICHA DO ALUNO
# ==================================================

# FOTO DO ALUNO (TÍTULO)

caminho_foto_aluno = (
    BASE_DIR
    / "img"
    / "class-edna-krabappel"
    / aluno_atual.foto
)

label_titulo_foto = tk.Label(
    janela,
    text="FOTO DO ALUNO",
    font=("Fredoka SemiBold", 12),
    bg="#fee686",
    fg="#114510"
)

label_titulo_foto.place(
    x=220,
    y=252,
    width=150
)

imagem_foto = Image.open(
    caminho_foto_aluno
)

# FOTO DO ALUNO

foto_aluno = ImageTk.PhotoImage(
    imagem_foto
)

label_foto = tk.Label(
    janela,
    image=foto_aluno,
    bd=0
)

label_foto.place(
    x=220,
    y=278
)

# NOME DO ALUNO

label_nome = tk.Label(
    janela,
    text="",
    font=("Arial", 12, "bold"),
    bg="#fee686",
    fg="#114510",
    width=15
)

label_nome.place(
    x=220,
    y=505
)

# NÚMERO DO ALUNO

label_numero = tk.Label(
    janela,
    text="",
    bg="white"
)

label_numero.place(
    x=220,
    y=500
)

# IDADE DO ALUNO

label_idade = tk.Label(
    janela,
    text="",
    bg="white"
)

label_idade.place(
    x=220,
    y=525
)

# CURSO DO ALUNO

label_curso = tk.Label(
    janela,
    text="",
    bg="white"
)

label_curso.place(
    x=220,
    y=550
)

# MÉDIA DO ALUNO

label_media = tk.Label(
    janela,
    text="",
    bg="white"
)

label_media.place(
    x=220,
    y=575
)

# ==================================================
# BOTÕES DA FICHA DO ALUNO
# ==================================================

# BOTÃO CARREGAR FOTO

botao_teste = tk.Button(
    janela,
    text="CARREGAR FOTO",
    command=carregar_foto
)

botao_teste.place(
    x=240,
    y=480
)

# BOTÃO ALUNO ANTERIOR

botao_anterior = tk.Button(
    janela,
    text="←"
)

botao_anterior.config(
    command=aluno_anterior
)

botao_anterior.place(
    x=220,
    y=520
)

# BOTÃO PRÓXIMO ALUNO

botao_proximo = tk.Button(
    janela,
    text="→"
)

botao_proximo.config(
    command=proximo_aluno
)

botao_proximo.place(
    x=320,
    y=520
)

# ==================================================
# INICIALIZAÇÃO
# ==================================================

mostrar_aluno()

# ==================================================
# LOOP PRINCIPAL
# ==================================================

janela.mainloop()