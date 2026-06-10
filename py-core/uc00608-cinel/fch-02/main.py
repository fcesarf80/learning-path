import tkinter as tk

from PIL import Image
from PIL import ImageTk


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

from pathlib import Path

BASE_DIR = Path(__file__).parent

caminho_fundo = BASE_DIR / "img" / "tela" / "background.png"

imagem_fundo = Image.open(caminho_fundo)

imagem_fundo = imagem_fundo.resize(
    (1366, 768)
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
# LOOP
# ==========================

janela.mainloop()