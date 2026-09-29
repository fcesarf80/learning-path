import tkinter as tk

from utils.background import aplicar_background
from PIL import Image, ImageTk
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService

livro_service = LivroService()
utilizador_service = UtilizadorService()

csv_emprestimos = CSVService("data/emprestimos.csv")
csv_historico = CSVService("data/historico.csv")

# ==========================================
# MENU LATERAL (COORDENADAS)
# ==========================================

MENU_X = 18
MENU_LARGURA = 90
MENU_ALTURA = 42

Y_DASHBOARD      = 121
Y_LIVROS         = 161
Y_UTILIZADORES   = 205
Y_EMPRESTIMOS    = 249
Y_DEVOLUCOES     = 292
Y_ATIVOS         = 333
Y_HISTORICO      = 374
Y_CSV            = 413
Y_ESTATISTICAS   = 456

# ==========================================
# INDICADORES (COORDENADAS)
# ==========================================

CARD_X_LIVROS = 385
CARD_X_UTILIZADORES = 615
CARD_X_EMPRESTIMOS = 845
CARD_X_HISTORICO = 1075

CARD_Y = 185

CARD_WIDTH = 90
CARD_HEIGHT = 60

def criar_tela_dashboard(parent):

    # Background
    aplicar_background(parent, "img/dashboard.png")
    seta = Image.open("img/seta.png")
    seta = seta.resize((16, 16))
    seta = ImageTk.PhotoImage(seta)

    # ==========================================
    # INDICADORES
    # ==========================================

    lbl_livros = tk.Label(
        parent,
        text=str(livro_service.quantidade_livros()),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eaf3fe",
        bd=0,
        anchor="center"
    )

    lbl_utilizadores = tk.Label(
        parent,
        text=str(utilizador_service.quantidade_utilizadores()),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#fef6e7",
        bd=0,
        anchor="center"
    )

    lbl_emprestimos = tk.Label(
        parent,
        text=str(len(csv_emprestimos.carregar_emprestimos())),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eff6ed",
        bd=0,
        anchor="center"
    )

    lbl_historico = tk.Label(
        parent,
        text=str(len(csv_historico.carregar_emprestimos())),
        font=("Segoe UI", 28, "bold"),
        fg="#2F3B52",
        bg="#eeecf9",
        bd=0,
        anchor="center"
    )

    # ==========================================
    # POSICIONAMENTO DOS INDICADORES
    # ==========================================
    
    lbl_livros.place(
        x=CARD_X_LIVROS,
        y=CARD_Y,
        width=CARD_WIDTH,
        height=CARD_HEIGHT
    )

    lbl_utilizadores.place(
        x=CARD_X_UTILIZADORES,
        y=CARD_Y,
        width=CARD_WIDTH,
        height=CARD_HEIGHT
    )

    lbl_emprestimos.place(
        x=CARD_X_EMPRESTIMOS,
        y=CARD_Y,
        width=CARD_WIDTH,
        height=CARD_HEIGHT
    )

    lbl_historico.place(
        x=CARD_X_HISTORICO,
        y=CARD_Y,
        width=CARD_WIDTH,
        height=CARD_HEIGHT
    )

    # ==========================================
    # ÍCONE DA SETA
    # ==========================================

    seta = Image.open("img/seta.png")
    seta = seta.resize((28, 28))
    seta = ImageTk.PhotoImage(seta)

    icone_dashboard = Image.open("img/seta.png")
    icone_dashboard = icone_dashboard.resize((28, 28))
    icone_dashboard = ImageTk.PhotoImage(icone_dashboard)

    # ==========================================
    # MENU LATERAL (ÁREAS CLICÁVEIS)
    # ==========================================

    # Dashboard
    area_dashboard = tk.Label(
    parent,
    image=icone_dashboard,
    bd=0,
    cursor="hand2"
    )

    area_dashboard.image = icone_dashboard

    area_dashboard.place(
        x=MENU_X,
        y=Y_DASHBOARD,
        width=24,
        height=24
    )

    area_dashboard.bind(
        "<Button-1>",
        lambda e: print("Dashboard")
    )

    # Livros
    area_livros = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_livros.place(
        x=MENU_X,
        y=Y_LIVROS,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_livros.bind(
        "<Button-1>",
        lambda e: print("Livros")
    )

    # Utilizadores
    area_utilizadores = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_utilizadores.place(
        x=MENU_X,
        y=Y_UTILIZADORES,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_utilizadores.bind(
        "<Button-1>",
        lambda e: print("Utilizadores")
    )

    # Emprestimos
    area_emprestimos = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_emprestimos.place(
        x=MENU_X,
        y=Y_EMPRESTIMOS,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_emprestimos.bind(
        "<Button-1>",
        lambda e: print("emprestimos")
    )


    # Devolucao
    area_devolucao = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_devolucao.place(
        x=MENU_X,
        y=Y_DEVOLUCOES,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_devolucao.bind(
        "<Button-1>",
        lambda e: print("Devoluções")
    )


    # Ativos
    area_ativos = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_ativos.place(
        x=MENU_X,
        y=Y_ATIVOS,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_ativos.bind(
        "<Button-1>",
        lambda e: print("Ativos")
    )


    # Historico
    area_historico = tk.Frame(
            parent,
            bg="",
            cursor="hand2"
        )

    area_historico.place(
        x=MENU_X,
        y=Y_HISTORICO,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_historico.bind(
        "<Button-1>",
        lambda e: print("historico")
    )

    #  CSV
    area_csv = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_csv.place(
        x=MENU_X,
        y=Y_CSV,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_csv.bind(
        "<Button-1>",
        lambda e: print("CSV")
    )

    # Estatisticas
    area_estatisticas = tk.Frame(
        parent,
        bg="",
        cursor="hand2"
    )

    area_estatisticas.place(
        x=MENU_X,
        y=Y_ESTATISTICAS,
        width=MENU_LARGURA,
        height=MENU_ALTURA
    )

    area_estatisticas.bind(
        "<Button-1>",
        lambda e: print("Estatisticas")
    )

