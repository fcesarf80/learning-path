"""
4) Dada uma frase como input, desenvolva uma função que determine a quantidade de carateres de pontuação (!?.), de letras maiúsculas e de letras minúsculas (os símbolos "º" e "ª" não devem ser considerados carateres minúsculos).
"""

def analise(frs):
    mai, min, num = 0, 0, 0
    for char in frs:
        if char.isupper():
            mai += 1
        elif char.islower():
            min += 1
        elif char in "!?.":
            num += 1
    return mai, min, num
frs = input("Digite uma frase: ")
mai, min, num = analise(frs)
print("Maiúsculas:", mai)
print("Minúsculas:", min)
print("Pontuação:", num)