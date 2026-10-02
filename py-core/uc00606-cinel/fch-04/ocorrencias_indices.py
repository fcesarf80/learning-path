"""
Exercício: Ocorrências e Índices
Recorrendo a uma função, procure um valor num tuplo. Apresente quantas vezes aparece, a primeira posição, a última posição e todas as posições onde aparece. Se não existir, apresente 0 e -1.
"""

def procurar(tuplo, valor):
    inds = ()

    # Percorre a tupla usando o índice (posição)
    for i in range(len(tuplo)):
        if tuplo[i] == valor:
            inds += (i,)

    # Se a tupla de índices estiver vazia, retorna None para indicar ausência
    if len(inds) == 0:
        return 0, None, None, ()

    # Se encontrar, retorna os dados reais
    return len(inds), inds[0], inds[-1], inds


# Código Principal
tuplo = (1, 2, 3, 4, 5, 6, 7)

valor = int(input("Digite o valor: "))

qtd, prim, ult, inds = procurar(tuplo, valor)

print(f"Ocorr.: {qtd} | Pos. enc.: {inds if inds else 'Nenhuma'}")
print(f"1º pos: {prim if prim is not None else 'N/A'} | Últ. pos.: {ult if ult is not None else 'N/A'}")
