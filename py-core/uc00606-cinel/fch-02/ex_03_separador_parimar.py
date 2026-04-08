"""
Exercício 3 – Separador pares-impares
Enunciado: 3. Crie uma função que dado um tuplo de valores inteiros positivos,
devolva dois novos tuplos, um de inteiros positivos pares e outro de inteiros positivos ímpares.
"""

from random import randint
def odd_even(tup):
    t_even, t_odd = (), () #2 tuplas vazias
    for elem in tup:
        if elem % 2==0: #elem é par
            t_even = t_even + (elem,)
        else:
            t_odd = t_odd + (elem,)
    return (t_even, t_odd)
tup = ()
for _ in range(20):
    tup = tup + (randint(1,100),)
par, impar = odd_even(tup) #((2,4,0), (3,7))
print(f"Os valores pares são: {tuple(sorted(par))}")
print(f"Os valores ímpares são: {tuple(sorted(impar))}")
