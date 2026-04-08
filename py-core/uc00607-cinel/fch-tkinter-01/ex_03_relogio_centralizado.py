"""
Exercício 03 - Relógio centro
Enunciado: Crie uma aplicação em Tkinter com uma label para mostrar
um relógio digital. Defina a fonte para Arial, tamanho 16 e negrito.
Importe da biblioteca time a função strftime.
Crie uma função “relogio” que atualize a label de 1000 em 1000 milissegundos,
utilizando after(1000, nome_func).
A janela deve arrancar no centro do ecrã, utilizando as funções
winfo_screenwidth() e winfo_screenheight().
"""

import tkinter as tk
from time import strftime



# Função do relógio
def relogio():
    hora_atual = strftime("%H:%M:%S")
    lbl_relogio.config(text=hora_atual)
    lbl_relogio.after(1000, relogio)

# Janela principal
janela = tk.Tk()
janela.title("Relógio Digital")
janela.config(bg="white")
janela.resizable(False, False)

# Tamanho da janela
largura_janela = 400
altura_janela = 200

# Dimensões do ecrã
largura_ecra = janela.winfo_screenwidth()
altura_ecra = janela.winfo_screenheight()

# Cálculo para centralizar
pos_x = (largura_ecra // 2) - (largura_janela // 2)
pos_y = (altura_ecra // 2) - (altura_janela // 2)

# Aplicar tamanho + posição
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


# Fonte
fonte_relogio = ("Arial", 16, "bold")

# Labels
lbl_titulo = tk.Label(
    janela,
    text="Hora atual:",
    font=("Arial", 14, "bold"),
    bg="white"
)
lbl_titulo.pack(pady=30)

lbl_relogio = tk.Label(
    janela,
    text="",
    font=fonte_relogio,
    bg="white",
    fg="blue"
)
lbl_relogio.place(x=260, y=150)

# Iniciar relógio

relogio()

# Loop principal
janela.mainloop()