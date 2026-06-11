import tkinter as tk

from tkinter import filedialog

from pathlib import Path

from PIL import Image
from PIL import ImageTk

from services.gestor_alunos import lista_alunos

print(
    f"Total de alunos: {len(lista_alunos)}"
)

# ==================================
# FUNÇÕES
# ==================================

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


# ==========================
# JANELA
# ==========================

janela = tk.Tk()

janela.title("Gestor de Alunos - Turma da Edna")
janela.geometry("1366x768")
janela.resizable(False, False)


# ==========================
# BACKGROUND
# ==========================



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


# ==========================
# FOTO VAZIA
# ==========================

caminho_foto_vazia = (
    BASE_DIR
    / "img"
    / "tela"
    / "foto_vazia.png"
)

imagem_foto = Image.open(
    caminho_foto_vazia
)

foto_vazia = ImageTk.PhotoImage(
    imagem_foto
)

label_foto = tk.Label(
    janela,
    image=foto_vazia,
    bd=0
)

label_foto.place(
    x=220,
    y=272
)

# ==================================
# BUTTON
# ==================================

botao_teste = tk.Button(
    janela,
    text="CARREGAR FOTO",
    command=carregar_foto
)

botao_teste.place(
    x=240,
    y=477
)


# ==========================
# LOOP
# ==========================

janela.mainloop()