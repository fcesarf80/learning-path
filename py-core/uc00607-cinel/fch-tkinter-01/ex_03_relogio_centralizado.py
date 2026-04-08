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


# =========================
# FUNÇÃO DO RELÓGIO
# =========================
def relogio():
    hora = strftime("%H:%M:%S")
    lbl_relogio.config(text=hora)
    lbl_relogio.after(1000, relogio)


# =========================
# JANELA
# =========================
janela = tk.Tk()
janela.title("Relógio Digital")
janela.config(bg="#1e1e1e")  # fundo escuro
janela.resizable(False, False)

largura = 400
altura = 200

screen_w = janela.winfo_screenwidth()
screen_h = janela.winfo_screenheight()

x = (screen_w // 2) - (largura // 2)
y = (screen_h // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{x}+{y}")


# =========================
# LABEL RELÓGIO (CENTRO)
# =========================
lbl_relogio = tk.Label(
    janela,
    font=("Arial", 36, "bold"),
    bg="#1e1e1e",
    fg="#00ff88"
)

lbl_relogio.pack(expand=True)


# =========================
# INICIAR
# =========================
relogio()

janela.mainloop()