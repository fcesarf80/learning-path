# IMPORTS

import tkinter as tk

from views.livros import criar_tela_livros
from views.utilizadores import criar_tela_utilizadores
from views.emprestimos import criar_tela_emprestimos
from views.devolucoes import criar_tela_devolucoes
from views.ativos import criar_tela_ativos
from views.historico import criar_tela_historico
from views.csv_view import criar_tela_csv
from views.estatisticas import criar_tela_estatisticas

from config import *

# Janela

LARGURA_JANELA = "1200x700"
TITULO_JANELA = "Gestor de Biblioteca"

# Menu

LARGURA_MENU = 300

# Fontes

FONTE_TITULO = ("Segoe UI", 20, "bold")
FONTE_SUBTITULO = ("Segoe UI", 14, "bold")
FONTE_NORMAL = ("Segoe UI", 10)
FONTE_CARD = ("Segoe UI", 20, "bold")

# FUNÇÕES

def criar_card(parent, numero, texto):

    card = tk.Frame(
        parent,
        bg="white",
        bd=1,
        relief="solid",
        width=180,
        height=100
    )

    card.pack_propagate(False)

    card.pack(
        side="left",
        padx=10
    )

    lbl_numero = tk.Label(
        card,
        text=numero,
        font=("Segoe UI", 20, "bold"),
        bg="white"
    )

    lbl_numero.pack(
        pady=(15, 5)
    )

    lbl_texto = tk.Label(
        card,
        text=texto,
        font=("Segoe UI", 10),
        bg="white"
    )

    lbl_texto.pack()


def criar_botao_dashboard(parent, texto):

    botao = tk.Button(
        parent,
        text=texto,
        width=18,
        height=3,
        bg=COR_BOTAO,
        relief="solid",
        bd=1
    )

    return botao

def limpar_conteudo():

    for widget in frame_conteudo.winfo_children():
        widget.destroy()

def abrir_livros():

    limpar_conteudo()
    criar_tela_livros(frame_conteudo)

def abrir_utilizadores():
    limpar_conteudo()
    criar_tela_utilizadores(frame_conteudo)

def abrir_emprestimos():
    limpar_conteudo()
    criar_tela_emprestimos(frame_conteudo)

def abrir_devolucoes():
    limpar_conteudo()
    criar_tela_devolucoes(frame_conteudo)

def abrir_ativos():
    limpar_conteudo()
    criar_tela_ativos(frame_conteudo)

def abrir_historico():
    limpar_conteudo()
    criar_tela_historico(frame_conteudo)

def abrir_csv():
    limpar_conteudo()
    criar_tela_csv(frame_conteudo)

def abrir_estatisticas():
    limpar_conteudo()
    criar_tela_estatisticas(frame_conteudo)

def abrir_dashboard():

    limpar_conteudo()

# reconstruir dashboard

# JANELA PRINCIPAL

janela = tk.Tk()

janela.title(TITULO_JANELA)
janela.geometry(LARGURA_JANELA)
janela.configure(bg=COR_FUNDO)

# MENU LATERAL

frame_menu = tk.Frame(
    janela,
    width=300,
    bg=COR_MENU
)

frame_menu.pack(
    side="left",
    fill="y"
)

titulo = tk.Label(
    frame_menu,
    text="📚 Biblioteca",
    font=("Segoe UI", 16, "bold"),
    bg=COR_MENU
)

titulo.pack(
    pady=20
)

menus = {
    "Dashboard": None, #abrir_dashboard,
    "Livros": abrir_livros,
    "Utilizadores": abrir_utilizadores,
    "Empréstimos": abrir_emprestimos,
    "Devoluções": abrir_devolucoes,
    "Ativos": abrir_ativos,
    "Histórico": abrir_historico,
    "CSV": abrir_csv,
    "Estatísticas": abrir_estatisticas
}

for texto, comando in menus.items():

    botao = tk.Button(
        frame_menu,
        text=texto,
        anchor="w",
        relief="flat",
        bg="#F5F7F7",
        padx=15,
        command=comando
    )

    botao.pack(
        fill="x",
        pady=2
    )

frame_conteudo = tk.Frame(
    janela,
    bg="white"
)

frame_conteudo.pack(
    side="right",
    expand=True,
    fill="both"
)

cabecalho = tk.Frame(
    frame_conteudo,
    bg="white",
    height=80
)

cabecalho.pack(
    fill="x"
)

titulo_dashboard = tk.Label(
    cabecalho,
    text="Dashboard",
    font=FONTE_TITULO,
    bg="white"
)

# DASHBOARD - CABEÇALHO

titulo_dashboard.pack(
    anchor="w",
    padx=30,
    pady=20
)

frame_cards = tk.Frame(
    frame_conteudo,
    bg="white"
)

frame_cards.pack(
    anchor="w",
    padx=30,
    pady=20
)

frame_acesso = tk.Frame(
    frame_conteudo,
    bg="white"
)

frame_acesso.pack(
    anchor="w",
    padx=30
)

# DASHBOARD - CARDS

criar_card(frame_cards, "128", "Livros")
criar_card(frame_cards, "56", "Utilizadores")
criar_card(frame_cards, "18", "Empréstimos")
criar_card(frame_cards, "325", "Histórico")

# DASHBOARD - ACESSO RÁPIDO

titulo_acesso = tk.Label(
    frame_conteudo,
    text="Acesso Rápido",
    font=FONTE_SUBTITULO,
    bg="white"
)

titulo_acesso.pack(
    anchor="w",
    padx=30,
    pady=(20,10)
)

linha1 = tk.Frame(
    frame_acesso,
    bg="white"
)

linha1.pack(
    pady=5
)

linha2 = tk.Frame(
    frame_acesso,
    bg="white"
)

linha2.pack(
    pady=5
)

criar_botao_dashboard(linha1, "Adicionar Livro").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Pesquisar Livro").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Empréstimo").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Devolução").pack(side="left", padx=5)

criar_botao_dashboard(linha2, "Utilizadores").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Ativos").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Histórico").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Estatísticas").pack(side="left", padx=5)

# DASHBOARD - ATIVIDADE RECENTE

titulo_atividade = tk.Label(
    frame_conteudo,
    text="Atividade Recente",
    font=("Segoe UI", 14, "bold"),
    bg="white"
)

titulo_atividade.pack(
    anchor="w",
    padx=30,
    pady=(25,10)
)

frame_atividade = tk.Frame(
    frame_conteudo,
    bg="white",
    bd=1,
    relief="solid"
)

frame_atividade.pack(
    fill="x",
    padx=30
)

atividades = [
    "📚 Livro 'O Hobbit' adicionado",
    "👤 Utilizador 'Maria Santos' criado",
    "📤 Empréstimo realizado",
    "📥 Devolução registada"
]

for atividade in atividades:

    lbl = tk.Label(
        frame_atividade,
        text=atividade,
        bg="white",
        anchor="w",
        font=FONTE_NORMAL
    )

    lbl.pack(
        anchor="w",
        padx=15,
        pady=5
    )

janela.mainloop()