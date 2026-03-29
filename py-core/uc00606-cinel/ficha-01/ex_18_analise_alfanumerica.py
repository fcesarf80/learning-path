"""
Exercício 18 - analise alfanumerico
Enunciado: Dada uma frase alfanumérica no input, pretende-se que implemente uma função que determine o número de carateres
maiúsculos, minúsculos e numéricos."""

def analisar_frase(frase):
    # Inicializamos os contadores
    maiusculos = 0
    minusculos = 0
    numeros = 0

    # Percorremos cada caractere da frase
    for caractere in frase:
        if caractere.isupper():
            maiusculos += 1
        elif caractere.islower():
            minusculos += 1
        elif caractere.isdigit():
            numeros += 1

    return maiusculos, minusculos, numeros

def executar():
    # Solicita a entrada do usuário
    entrada = input("Digite uma frase alfanumérica: ")

    # Chama a função e desempacota os resultados
    mai, min, num = analisar_frase(entrada)

    # Exibe os resultados
    print(f"\nAnálise da frase:")
    print(f"- Letras maiúsculas: {mai}")
    print(f"- Letras minúsculas: {min}")
    print(f"- Caracteres numéricos: {num}")
    print(f"- Total de caracteres: {len(entrada)}")

if __name__ == "__main__":
    executar() 