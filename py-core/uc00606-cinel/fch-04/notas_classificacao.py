"""
Exercício: Notas e Classificação
Enunciado:Leia 5 notas entre 0 e 20, calcule a média e apresente a classificação:
menor que 10 → Mau
menor que 14 → Médio
até 18 → Bom
acima de 18 → Muito Bom
"""

def classificar(media):
    if media < 10:
        return "Mau"
    elif media < 14:
        return "Médio"
    elif media <= 18:
        return "Bom"
    else:
        return "Muito Bom"


soma = 0

for i in range(5):
    nota = float(input("Nota: "))
    soma += nota

media = soma / 5

print("Média:", media)
print("Classificação:", classificar(media))