"""
Exercício 05 - Media notas
Enunciado: Dadas 5 notas finais de avaliação de um aluno (de 0 a 20), determine se este é
'mau', 'médio', 'bom' ou 'muito bom' aluno tendo em consideração a seguinte tabela:
a. Mau se a média é inferior a 10;           c. Bom se a média está compreendida entre 14 e 18
b. Muito bom se a média é superior a 18;     d. Médio se a média for positiva mas inferior a 14.
"""

n_notas = int(input("Quantas notas deseja inserir? "))
notas = []

for qt in range(1, n_notas + 1):
    valor = -1
    while (valor < 0) or (valor > 20):
        # Entrada de dados do usuário
        valor = float(input(f"Insira a {qt}ª nota (0-20): "))
    
    notas.append(valor)

# Cálculo automático com base no que foi inserido
media = sum(notas) / len(notas)

print(f"\nNotas: {notas}")
if media < 10:
    print(f"Média {media:.1f} -> Mau")
elif media < 14:
    print(f"Média {media:.1f} -> Médio")
elif media <= 18:
    print(f"Média {media:.1f} -> Bom")
else:
    print(f"Média {media:.1f} -> Muito Bom")
