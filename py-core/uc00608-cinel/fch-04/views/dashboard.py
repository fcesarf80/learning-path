import tkinter as tk

from config import *

from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService

# UTILITÁRIOS DA INTERFACE
def criar_card(parent, numero, texto):
    card = tk.Frame(
        parent,
        bg=COR_FUNDO,
        bd=1,
        relief="solid",
        width=180,
        height=100,
        highlightbackground=COR_BORDA
    )
    card.pack_propagate(False)
    card.pack(side="left", padx=10)
    
    lbl_numero = tk.Label(
        card,
        text=numero,
        font=FONTE_CARD,
        bg=COR_FUNDO
    )
    lbl_numero.pack(pady=(15, 5))
    
    lbl_texto = tk.Label(
        card,
        text=texto,
        font=FONTE_NORMAL,
        bg=COR_FUNDO
    )
    lbl_texto.pack()

def criar_botao_dashboard(parent, texto):
    return tk.Button(
        parent,
        text=texto,
        width=18,
        height=3,
        bg=COR_BOTAO,
        font=FONTE_NORMAL,
        relief="solid",
        bd=1
    )
