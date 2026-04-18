"""
exercício 09 - Leia salário e calcule bônus:
2000 → +10% e <= 2000 → +5%
"""
valor = int(input("Digite o salário: "))
if valor > 2000:
    bonus = valor * 0.10
else:
    bonus = valor * 0.05
valor_final = valor + bonus
print(f"Salário: {valor}")
print(f"Bônus: {bonus}")
print(f"Total: {valor_final}")