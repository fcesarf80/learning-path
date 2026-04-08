"""
Exercício 17 - Contagem caracteres
Enunciado: Dada uma frase no input, pretende-se que implemente uma
# função que determine o número de carateres que esta contém.
# O mesmo que faz a função len().
"""

def contar_caracteres(frase):
    contador = 0
    # Percorre cada elemento dentro da string
    for caractere in frase:
        contador += 1
    return contador

def programa_principal():
    # Solicita a frase ao usuário
    entrada = input("Digite uma frase: ")

    # Chama a função personalizada
    total = contar_caracteres(entrada)

    print(f"A frase contém {total} caracteres.")

# Executa o programa
if __name__ == "__main__":
    programa_principal()