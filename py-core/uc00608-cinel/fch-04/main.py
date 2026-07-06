import tkinter as tk
from tkinter import ttk
from views.dashboard import criar_tela_dashboard
from views.livros import criar_tela_livros
from views.utilizadores import criar_tela_utilizadores
from views.emprestimos import criar_tela_emprestimos
from views.devolucoes import criar_tela_devolucoes
from views.ativos import criar_tela_ativos
from views.historico import criar_tela_historico
from views.csv_view import criar_tela_csv
from views.estatisticas import criar_tela_estatisticas
from services.livro_service import LivroService
from services.utilizador_service import UtilizadorService
from services.csv_service import CSVService
from config import *

# INICIALIZA OS SERVICES
livro_service = LivroService()
utilizador_service = UtilizadorService()

csv_emprestimos = CSVService(
    "data/emprestimos.csv"
)
csv_historico = CSVService(
    "data/historico.csv"
)

# CONFIGURAÇÕES
LARGURA_JANELA = "1280x720"
TITULO_JANELA = "Gestor de Biblioteca"

# UTILITÁRIOS DA INTERFACE


def limpar_conteudo():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

# NAVEGAÇÃO
def abrir_dashboard():
    limpar_conteudo()
    criar_tela_dashboard(frame_conteudo)

def abrir_livros():
    limpar_conteudo()
    criar_tela_livros(
        frame_conteudo
    )

def abrir_utilizadores():
    limpar_conteudo()
    criar_tela_utilizadores(
        frame_conteudo
    )

def abrir_emprestimos():
    limpar_conteudo()
    criar_tela_emprestimos(
        frame_conteudo
    )

def abrir_devolucoes():
    limpar_conteudo()
    criar_tela_devolucoes(
        frame_conteudo
    )

def abrir_ativos():
    limpar_conteudo()
    criar_tela_ativos(
        frame_conteudo
    )

def abrir_historico():
    limpar_conteudo()
    criar_tela_historico(
        frame_conteudo
    )

def abrir_csv():
    limpar_conteudo()
    criar_tela_csv(
        frame_conteudo
    )

def abrir_estatisticas():
    limpar_conteudo()
    criar_tela_estatisticas(
        frame_conteudo
    )


# JANELA PRINCIPAL
janela = tk.Tk()
janela.iconbitmap("img/cinel.ico")

janela.title(TITULO_JANELA)
janela.geometry(LARGURA_JANELA)
janela.resizable(False, False)
janela.configure(bg=COR_FUNDO)




# # MENU LATERAL
# frame_menu = tk.Frame(
#     janela, 
#     width=300, 
#     bg=COR_MENU
# )
# frame_menu.pack(
#     side="left", 
#     fill="y"
# )

# lbl_logo = tk.Label(
#     frame_menu,
#     text="📚 Biblioteca",
#     font=("Segoe UI", 16, "bold"),
#     bg=COR_MENU
# )
# lbl_logo.pack(
#     pady=20
# )


# for texto, comando in menus.items():
#     botao = tk.Button(
#         frame_menu,
#         text=texto,
#         anchor="w",
#         relief="flat",
#         bg=COR_MENU,
#         font=FONTE_NORMAL,
#         padx=15,
#         command=comando
#     )
#     botao.pack(
#         fill="x", 
#         pady=2
#     )

# CONTEÚDO
frame_conteudo = tk.Frame(
    janela, 
    bg=COR_FUNDO
)
frame_conteudo.pack(
    expand=True,
    fill="both"
)

abrir_dashboard()

janela.mainloop()
