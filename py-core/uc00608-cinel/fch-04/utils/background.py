import tkinter as tk
from PIL import Image, ImageTk


def aplicar_background(parent, caminho):
    imagem = Image.open(caminho)
    imagem = imagem.resize((1280, 720))

    photo = ImageTk.PhotoImage(imagem)

    fundo = tk.Label(parent, image=photo)
    fundo.image = photo
    fundo.place(x=0, y=0)

    return fundo