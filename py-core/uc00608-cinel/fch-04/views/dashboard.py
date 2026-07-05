import tkinter as tk

from config import *

from PIL import Image, ImageTk
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService

livro_service = LivroService()
utilizador_service = UtilizadorService()

csv_emprestimos = CSVService(
    "data/emprestimos.csv"
)

csv_historico = CSVService(
    "data/historico.csv"
)

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

def criar_tela_dashboard(parent):

    imagem = Image.open("img/dashboard.png")
    imagem = imagem.resize((1280, 720))

    bg = ImageTk.PhotoImage(imagem)

    # DASHBOARD: CABEÇALHO
    cabecalho = tk.Frame(
        parent,
        bg=COR_FUNDO,
        height=80
    )
    cabecalho.pack(
        fill="x"
    )

    titulo_dashboard = tk.Label(
        cabecalho,
        text="Dashboard",
        font=FONTE_TITULO,
        bg=COR_FUNDO
    )
    titulo_dashboard.pack(
        anchor="w", 
        padx=30, 
        pady=20
    )

    # DASHBOARD: CARDS
    frame_cards = tk.Frame(
        parent,
        bg=COR_FUNDO
    )
    frame_cards.pack(
        anchor="w", 
        padx=30, 
        pady=20
    )

    criar_card(
        frame_cards,
        str(livro_service.quantidade_livros()),
        "Livros"
    )

    criar_card(
        frame_cards,
        str(utilizador_service.quantidade_utilizadores()),
        "Utilizadores"
    )

    criar_card(
        frame_cards,
        str(len(csv_emprestimos.carregar_emprestimos())),
        "Empréstimos"
    )

    criar_card(
        frame_cards,
        str(len(csv_historico.carregar_emprestimos())),
        "Histórico"
    )
