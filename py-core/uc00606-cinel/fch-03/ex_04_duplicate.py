"""
Exercicio_04_duplicate.py: Transformação de sequências através da duplicação de elementos.
Enunciado: 4. Escreva uma função duplicate(tup) que, dada uma tupla tup, retorne uma nova
tupla com todos os seus valores duplicados. Por exemplo, a tupla (1,2,3) deve dar origem
à tupla (1,1,2,2,3,3). Restrições: Os seguintes limites são garantidos em todos os casos
de teste que serão dados ao seu programa: 1 ≤ |tup| ≤ 100	- tamanho da tupla de entrada
Ex: print(duplicate( (1,2,3) )) - Saída: (1, 1, 2, 2, 3, 3)
Ex: print(duplicate( ("python","rocks") )) - Saída: ('python', 'python', 'rocks', 'rocks')
Ex: print(duplicate( (1.0, Verdadeiro, 4, "a") )) - Saída: (1.0, 1.0, True, True, 4, 4, 'a', 'a')
"""

def duplicate(tup):
    nova_t = ()
    for elem in tup:
        nova_t = nova_t + (elem,elem)

    return nova_t
print(duplicate ( (5,"rocks") ))
