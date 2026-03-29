"""
Exercicio 05 – Remove all
Enunciado: 5. Escreva uma função remove_all(word, ch) que, dada uma string word
constituída por letras minúsculas e uma letra minúscula ch, retorne uma nova
string igual à original, mas com todas as ocorrências do caractere ch removidas.
Restrições: Os seguintes limites são garantidos em todos os casos de teste que
serão fornecidos ao seu programa:1 ≤ |palavra| ≤ 100	tamanho da string de entrada
Exe: print(remove_all("suspeito", "s"))	Saída: upect
Ex: print(remove_all("metallica", "l"))	Saída: metaica
Ex: print(remove_all("abracadabra", "a"))	Saída: brcdbr
"""

def remove_all(frase, letra):
    nova_s = ""
    for elem in frase: #abracadabra
        if elem != letra: #quero guardar o elem
            nova_s += elem
    return nova_s 
    # return frase.replace(letra,"")
print(remove_all("abracadabra", "a"))
