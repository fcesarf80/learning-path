"""
Exercício 16 - Gerador aleatorios timer
Enunciado: Implemente uma função para cálculo do fatorial de forma recursiva.
"""

def potencia(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / potencia(x, -y)
    else:
        return x * potencia(x, y - 1)
    
try:
    # Captura as entradas do utilizador
    base = float(input("Digite a base (x): "))
    expoente = int(input("Digite o expoente inteiro (y): "))

    resultado = potencia(base, expoente)
    
    # Formatação para evitar muitas casas decimais em potências negativas
    print(f"{base} elevado a {expoente} é {resultado:.4f}" if expoente < 0 else f"{base} elevado a {expoente} é {resultado}")

except ValueError:
    print("Erro: Certifique-se de digitar números válidos (o expoente deve ser inteiro).")
except ZeroDivisionError:
    print("Erro: Não é possível elevar zero a um expoente negativo.")