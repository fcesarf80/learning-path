import tkinter as tk
from PIL import Image, ImageTk


def aplicar_background(parent, caminho_imagem):

    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((1280, 720))

    bg = ImageTk.PhotoImage(imagem)

    lbl = tk.Label(parent, image=bg, bd=0)
    lbl.image = bg
    lbl.place(x=0, y=0)