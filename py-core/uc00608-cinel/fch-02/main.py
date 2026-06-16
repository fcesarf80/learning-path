# ==================================================
# IMPORTS
# ==================================================

import tkinter as tk

from tkinter import ttk
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
# CAMINHOS DAS IMAGENS
# ==================================================

BASE_DIR = Path(__file__).parent

caminho_fundo = (
    BASE_DIR
    / "img"
    / "tela"
    / "background.png"
)

caminho_foto_vazia = (
    BASE_DIR
    / "img"
    / "tela"
    / "foto_vazia.png"
)

caminho_seta_esquerda = (
    BASE_DIR
    / "img"
    / "tela"
    / "mao-indicador-esquerda.png"
)

caminho_seta_direita = (
    BASE_DIR
    / "img"
    / "tela"
    / "mao-indicador-direita.png"
)

caminho_camera = (
    BASE_DIR
    / "img"
    / "tela"
    / "maquina_fotografica.png"
)

# MONTA O CAMINHO DA FOTO

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

def listar_alunos():

    for aluno in lista_alunos:

        tree_alunos.insert(
            "",
            "end",
            values=(
                aluno.numero,
                aluno.nome,
                aluno.sobrenome,
                aluno.idade,
                aluno.media
            )
        )

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

imagem_fundo = Image.open(
    caminho_fundo
)

imagem_fundo = imagem_fundo.resize(
    (1112, 743)
)

fundo = ImageTk.PhotoImage(
    imagem_fundo
)

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
    font=("Fredoka SemiBold", 12, "bold"),
    bg="#fee686",
    fg="#114510",
    width=15
)

label_nome.place(
    x=220,
    y=475
)

# NÚMERO DO ALUNO

label_numero = tk.Label(
    janela,
    text="",
    font=("Fredoka semibold", 10),
    bg="#fee686",
    fg="#114510"
)

label_numero.place(
    x=220,
    y=525
)

# IDADE DO ALUNO

label_idade = tk.Label(
    janela,
    text="",
    font=("Fredoka semibold", 10),
    bg="#fee686",
    fg="#114510"
)

label_idade.place(
    x=255,
    y=525
)

# CURSO DO ALUNO

label_curso = tk.Label(
    janela,
    text="",
    font=("Fredoka semibold", 10),
    bg="#fee686",
    fg="#114510"
)

label_curso.place(
    x=220,
    y=550
)

# MÉDIA DO ALUNO

label_media = tk.Label(
    janela,
    text="",
    font=("Fredoka semibold", 10),
    bg="#fee686",
    fg="#114510"
)

label_media.place(
    x=313,
    y=525
)

# ==================================================
# ÍCONES
# ==================================================

imagem_seta_esquerda = Image.open(
    caminho_seta_esquerda
)

imagem_seta_esquerda = imagem_seta_esquerda.resize(
    (36, 36)
)

icone_seta_esquerda = ImageTk.PhotoImage(
    imagem_seta_esquerda
)

imagem_seta_direita = Image.open(
    caminho_seta_direita
)

imagem_seta_direita = imagem_seta_direita.resize(
    (36, 36)
)

icone_seta_direita = ImageTk.PhotoImage(
    imagem_seta_direita
)

imagem_camera = Image.open(
    caminho_camera
)

imagem_camera = imagem_camera.resize(
    (36, 36)
)

icone_camera = ImageTk.PhotoImage(
    imagem_camera
)

# ==================================================
# BOTÕES DA FICHA DO ALUNO
# ==================================================

# BOTÃO CARREGAR FOTO

botao_carregar_foto = tk.Button(
    janela,
    image=icone_camera,
    command=carregar_foto,
    bg="#fee686",
    bd=0,
    highlightthickness=0
)

botao_carregar_foto.place(
    x=270,
    y=493
)

# BOTÃO ALUNO ANTERIOR

botao_anterior = tk.Button(
    janela,
    image=icone_seta_esquerda,
    command=aluno_anterior,
    bg="#fee686",
    bd=0,
    highlightthickness=0
)

botao_anterior.place(
    x=210,
    y=493
)

# BOTÃO PRÓXIMO ALUNO

botao_proximo = tk.Button(
    janela,
    image=icone_seta_direita,
    command=proximo_aluno,
    bg="#fee686",
    bd=0,
    highlightthickness=0
)

botao_proximo.place(
    x=330,
    y=493
)

# ==================================================
# GRELHA DE ALUNOS
# ==================================================

tree_alunos = ttk.Treeview(
    janela,
    columns=(
        "numero",
        "nome",
        "sobrenome",
        "idade",
        "media"
    ),
    show="headings"
)

tree_alunos.place(
    x=421,
    y=470,
    width=700,
    height=150
)

# CABEÇALHO

tree_alunos.heading(
    "numero",
    text="Nº"
)

tree_alunos.heading(
    "nome",
    text="Nome"
)

tree_alunos.heading(
    "sobrenome",
    text="Sobrenome"
)

tree_alunos.heading(
    "idade",
    text="Idade"
)

tree_alunos.heading(
    "media",
    text="Média"
)

# LARGURAS

tree_alunos.column(
    "numero",
    width=50
)

tree_alunos.column(
    "nome",
    width=180
)

tree_alunos.column(
    "sobrenome",
    width=180
)

tree_alunos.column(
    "idade",
    width=80
)

tree_alunos.column(
    "media",
    width=80
)

# REGISTROS

# ==================================================
# INICIALIZAÇÃO
# ==================================================

mostrar_aluno()

listar_alunos()

# ==================================================
# LOOP PRINCIPAL
# ==================================================

janela.mainloop()