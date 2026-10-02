"""
1) Ler 2 valores float diferentes de zero e devolver como OUTPUT:
• A soma dos 2 valores;             • A diferença dos 2 valores;
• O produto entre os 2 valores;     • O quociente e o resto da divisão entre os 2 valores.
"""

val1 = float(input("Digite o 1º valor: "))
val2 = float(input("Digite o 2º valor: "))
print("Soma:", val1 + val2, "Diferença:", val1 - val2)
print("Produto:", val1 * val2, "Quociente:", val1 / val2)
print("Resto:", val1 % val2)