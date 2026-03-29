"""
Exercício 11 - MDC algoritimo
Enunciado: Dados 2 valores inteiros m e n, diferentes de zero, implemente uma função que determine
o máximo divisor comum entre eles. Ex: mdc(24, 16) = 8, ou seja, 8 é o maior inteiro possível que divide ambos.
"""

def mdc(n1,n2):
  #x = min(n1, n2)
  if n1 < n2:
    x = n1
  else:
    x = n2

  while x > 0:
    if ( n1 % x == 0 ) and ( n2 % x == 0):
      return x

    x = x - 1


############
n1,n2 = int(input("Insira 2 valores inteiros: ")), int(input())
result = mdc(n1,n2)
print(f"mdc({n1},{n2}) = {result}")
