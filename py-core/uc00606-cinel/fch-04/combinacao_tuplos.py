"""
7 Exercício: Combinação de Tuplos
Enunciado: Recorrendo a funções, some dois tuplos elemento a elemento e determine os caracteres que existem em ambos os tuplos.
"""

def somar(t1, t2):
    res = ()

    for i in range(len(t1)):
        res += (t1[i] + t2[i],)

    return res


def comuns(t1, t2):
    res = ()

    for x in t1:
        if x in t2 and x not in res:
            res += (x,)

    return res


t1, t2 = (1, 2, 3), (4, 5, 6)


print("Soma:", somar(t1, t2))

t1, t2 = input("Digite as duas palavras (separadas por espaço): ").split()

print("Caracteres comuns:", comuns(t1, t2))