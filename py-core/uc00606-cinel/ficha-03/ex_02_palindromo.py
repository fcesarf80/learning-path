"""
Exercicio 02  - Palindromo
Enunciado: 2. Escreva uma função palíndromo(palavra) que, dada uma string palavra
constituída por letras minúsculas, retorne Verdadeiro se a palavra for um palíndromo
e Falso se não for. Restrições: Os seguintes limites são garantidos em todos os casos
de teste que serão dados ao seu programa:1 ≤ |palavra| ≤ 100		--  tamanho da string de entrada
"""

def palindrome(frase):
    if frase.lower() == frase[::-1].lower():
        return True
    return False

frase = input("Escreva algo: ")

#validação 1 ≤ |palavra| ≤ 100
while len(frase)==0 or len(frase)>100:
    frase = input("Escreva algo: ")

print(palindrome(frase))
