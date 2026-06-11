import tkinter as tk

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

def teste_botao():
    print("Botão clicado!")


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
    y=280
)

# ==================================
# BUTTON
# ==================================

botao_teste = tk.Button(
    janela,
    text="CARREGAR FOTO",
    command=teste_botao
)

botao_teste.place(
    x=240,
    y=450
)


# ==========================
# LOOP
# ==========================

janela.mainloop()