# 11 Exercício Primos - Elementosprimos tup
# Recorrendo a funções, dtrm se um núm int é primo ou não. De seguida, crie um tup com 20 núm aleatórios entre 2 e 100 e apresent os elem primos existentes nss tup.

from random import randint
def eh_primo(n):#Dtrm se núm int é primo.    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def primos(tup):    #Fltr e rtrn os elem primos d1 tup
    return tuple(elem for elem in tup if eh_primo(elem))
num = int(input("dgt núm: "))
if eh_primo(num):
    print(f"{num} é primo.")
else:
    print(f"{num} ñ é primo.")
tup = tuple(randint(2, 100) for _ in range(20)) #2. Cria tup c/20 núm aleatórios entre 2e 100
print(f"Tuplo: {tup}\nPrimos: {primos(tup)}")