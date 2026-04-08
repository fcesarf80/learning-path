"""
Exercício 9 - Potência manual
Enunciado: Implemente a função pot que recebe 2 argumentos dados pelo utilizador e devolve a potência entre ambos. Ex: pot(2,3) = 23=8
"""

# --- Definição das Funções ---

def pot(base, expoente):
    ## ---Calcula a potência de uma base elevada a um expoente.---
    return base ** expoente

def fat(n):
    ##--Calcula o fatorial de n de forma correta.--
    prod = 1
    for cont in range(1, n + 1):
        prod = prod * cont
    return prod  # O return deve estar FORA do ciclo for

# --- Execução do Programa ---

try:
    # Pedir valores ao utilizador (separados por espaço)
    valores = input("Insira a base e o expoente separados por espaço (ex: 2 3): ")
    info = valores.split()

    if len(info) < 2:
        print("Erro: Precisa de inserir dois números.")
    else:
        base = int(info[0])
        exp = int(info[1])

        # Chamar a função pot
        resultado_pot = pot(base, exp)
        print(f"-> {base} elevado a {exp} é: {resultado_pot}")

        # Exemplo extra: Fatorial da base
        if base >= 0:
            print(f"-> O fatorial de {base} é: {fat(base)}")
        else:
            print("-> Não existe fatorial de números negativos.")

except ValueError:
    print("Erro: Certifique-se de que inseriu números inteiros válidos.")
except IndexError:
    print("Erro: Formato de entrada inválido.")