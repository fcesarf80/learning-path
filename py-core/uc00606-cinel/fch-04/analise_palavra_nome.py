# 10 Exercício: Analise palavra nome
#  1. Dada uma string, apresente o primeiro e último elemento. Quando a entrada for uma palavra, apresente também os caracteres existentes entre o primeiro e o último. Quando a entrada for um nome completo, apresente o primeiro e o último nome.


def char(frase):
    prim, ult, mei = frase[0], frase[-1], frase[1:-1]
    return prim, ult, mei

def nomes(frase):
    partes = frase.split()

    prim, ult, mei = partes[0], partes[-1], " ".join(partes[1:-1])     

    return prim, ult, mei # Agora devolve as 3 partes!

frase = input("Introduza uma palavra ou nome completo: ")

if " " in frase:
    print(nomes(frase))
else:
    print(char(frase))