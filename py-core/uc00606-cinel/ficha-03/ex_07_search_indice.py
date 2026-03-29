"""
Exercicio 7 – Search indices
Enunciado: 7. Escreva uma função search(tup, value) que, dada uma tupla tup e um valor,
retorne uma tupla (first,last), respectivamente a primeira e a última posição do índice
onde o valor aparece (os índices começam com zero, é claro). Se o valor não aparecer,
retorne (-1,-1). Por exemplo, a tupla (1,2,1,2,1) tem o valor 1 em três posições:
0, 2 e 4, então search((1,2,1,2,1),1) deve retornar (0,4), o primeiro e o último índice.
Restrições: Os seguintes limites são garantidos em todos os casos de teste que serão
fornecidos ao seu programa:1 ≤ |tup| ≤ 100		tamanho da tupla de entrada
Ex: print(search( (1,2,1,2,1), 1 )) Saída: (0, 4)
Ex: imprimir(pesquisar( ("a","b","b","c"), "b" ))Saída: (1, 2)
Ex: imprimir(pesquisar( ("a","b","b","c"), "c" ))Saída: (3, 3)
Ex; imprimir(pesquisar( (True, True, True), False)) Saída: (-1,-1)
"""

def search(tup, value):
    # Se o valor não estiver na tupla, retorna (-1, -1)
    if value not in tup:
        return (-1, -1)
    
    # index(value) encontra a primeira ocorrência
    first = tup.index(value)
    
    # Para o último, percorremos a tupla de trás para frente
    # ou usamos o tamanho da tupla menos a posição na tupla invertida
    last = len(tup) - 1 - tup[::-1].index(value)
    
    return (first, last)

# Testes do enunciado:
print(search((1, 2, 1, 2, 1), 1))           
print(search(("a", "b", "b", "c"), "b"))     
print(search(("a", "b", "b", "c"), "c"))    
print(search((True, True, True), False))    
