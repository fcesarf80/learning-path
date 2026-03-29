"""
Exercício 01 - Gestão ficheiro
Enunciado: Crie um programa que solicite ao utilizador o seu nome completo.
Em seguida pretende-se guardar esse nome num ficheiro com o nome “texto.txt”.
Se o ficheiro “texto.txt” já existir, deverá removê-lo e criá-lo de novo sem dados.
"""
import os

def exercicio_01():
    # 1. Pega a pasta onde o script está rodando agora
    diretorio = os.getcwd() 
    
    # 2. Define o nome do arquivo dentro dessa pasta
    caminho_final = os.path.join(diretorio, "texto.txt")

    # 3. Garante que a pasta exista (embora o getcwd já garanta isso)
    os.makedirs(diretorio, exist_ok=True)

    # 4. Solicitar o nome
    nome_completo = input("Por favor, digite o seu nome completo: ")

    # 5. Lógica de remoção
    if os.path.exists(caminho_final):
        os.remove(caminho_final)
        print("Aviso: O ficheiro antigo foi removido.")

    # 6. Guardar o nome
    with open(caminho_final, "w", encoding="utf-8") as ficheiro:
        ficheiro.write(nome_completo)
    
    # 7. Feedback
    print(f"\nMuito prazer em conhecer-te, {nome_completo}!")
    print(f"O ficheiro foi guardado em: {caminho_final}\n")

# Executar o programa
exercicio_01()

