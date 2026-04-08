"""
Exercício 6 – Soma posicional tuplo
Enunciado: 6. Dados 2 tuplos com o mesmo número de elementos, pretendemos que criar um programa que faça a soma dos 
seus elementos em cada posição. Por exemplo, t1 = (2,5,3), t2 = (5,0,2), o resultado é (2+5, 5+0, 3+2) = (7,5,5).
"""

def ler_tupla(mensagem):
    while True:
        try:
            entrada = input(mensagem).split()
            # Tenta converter cada item para inteiro. Se falhar, vai para o 'except'
            return tuple(int(x) for x in entrada)
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros separados por espaços.")

# --- Início do Programa ---

t1 = ler_tupla("Digite os valores da primeira tupla: ")
t2 = ler_tupla("Digite os valores da segunda tupla: ")
t3 = ()

if len(t1) != len(t2):
    print("⚠️ As tuplas não têm o mesmo tamanho!")
    exit()

# Lógica de soma (exemplo com FOR)
for ind in range(len(t1)):
    x = t1[ind] + t2[ind]
    t3 += (x,)

print(f"\nResultado: {t1} + {t2} = {t3}")

