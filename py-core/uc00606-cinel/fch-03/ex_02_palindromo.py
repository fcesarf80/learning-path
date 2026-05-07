"""
Exercicio 02 - Palindromo
Enunciado: Escreva uma função palíndromo(palavra) que, dada uma string palavra
constituída por letras minúsculas, retorne True se a palavra for um palíndromo
e False se não for. Restrições: os seguintes limites devem ser garantidos em
todos os casos de teste, ao seu programa: 1 ≤ |palavra| ≤ 100
"""
def palindrome(frase):
    if frase.lower() == frase[::-1].lower():
        return True
    return False
frase = input("Escreva algo: ")
while len(frase)==0 or len(frase)>100:
    frase = input("Escreva algo: ")
print(palindrome(frase))