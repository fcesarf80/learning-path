"""
Exercício 02 - Junta ficheiros
Enunciado: Crie 2 ficheiros de texto com algo escrito em ambos.
Desenvolva um programa que solicite o nome dos 2 ficheiros ao utilizador.
Crie a função junta_fch() que recebe os 2 nomes como argumentos.
A função deverá criar o ficheiro de saída com a concatenação dos 2 ficheiros.
O nome do ficheiro de saída deverá ser solicitado ao utilizador.
"""

import os

# 2.3 - A FUNÇÃO (O Robô que recebe os nomes e trabalha)
def junta_fch(nome_arq1, nome_arq2, nome_saida):
    # Definimos onde os arquivos estão (sua pasta do Bloco 1)
    pasta = r"C:\Users\fcesa\Documents\MeusProjetosGitHub\projects\python-projects\01-python-estudos\UC00607-CINEL\ficha_01\Bloco 1 - Manipulação Básica de Arquivos"
    
    # Criamos os caminhos completos para o Windows não se perder
    caminho1 = os.path.join(pasta, nome_arq1)
    caminho2 = os.path.join(pasta, nome_arq2)
    caminho_final = os.path.join(pasta, nome_saida)

    # 2.4 - A "Mágica" de ler dois e escrever em um
    # Abrimos os dois primeiros para LEITURA ('r') e o terceiro para ESCRITA ('w')
    with open(caminho1, "r", encoding="utf-8") as f1, \
         open(caminho2, "r", encoding="utf-8") as f2, \
         open(caminho_final, "w", encoding="utf-8") as f_out:
        
        # O robô lê o conteúdo de f1 e f2 e coloca no f_out
        conteudo_total = f1.read() + "\n" + f2.read()
        f_out.write(conteudo_total)
    
    print(f"\nSucesso! O novo arquivo '{nome_saida}' foi criado com a união dos outros dois.")

def exercicio_02():
    print("--- Unificador de Arquivos ---")
    
    # 2.2 - Solicitar os nomes ao utilizador
    arquivo1 = input("Digite o nome do primeiro arquivo que já existe: ")
    arquivo2 = input("Digite o nome do segundo arquivo que já existe: ")
    arquivo_novo = input("Qual será o nome do novo arquivo de saída? ")

    # Chama a função enviando os 3 nomes como argumentos
    junta_fch(arquivo1, arquivo2, arquivo_novo)

# Chama o programa principal
exercicio_02()
