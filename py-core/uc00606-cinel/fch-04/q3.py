"""
3) O programa deverá, através de um ciclo, solicitar ao utilizador 5 valores inteiros positivos entre 0 e 20. Para cada valor corretamente lido, o programa deverá guardar os valores numa tupla e determinar o maior e o menor elemento desta tupla.
"""

val = ()
for i in range(5):
    num = int(input("Digite um valor entre 0 e 20: "))    
    while num < 0 or num > 20:
        num = int(input("Valor inválido. Digite valor entre 0 e 20: "))    
    val += (num,)
print(f"Tupla: {val}")
print(f"Maior: {max(val)}\nMenor: {min(val)}")