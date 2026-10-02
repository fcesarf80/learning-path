"""
Exercício: Operações com Valores
Enunciado: Crie funções para:
converter euros para dólares;
calcular a área, o perímetro e a quantidade de tinta de uma parede;
calcular o valor de um desconto e o preço final.
"""

def moeda(euros, taxa):
    return euros * taxa


def parede(largura, altura, tinta):
    area = largura * altura
    perimetro = 2 * (largura + altura)
    quantidade = area * tinta
    return area, perimetro, quantidade


def desconto(preco, percentagem):
    valor = preco * percentagem / 100
    final = preco - valor
    return valor, final


euros = float(input("Euros: "))
taxa = float(input("Taxa: "))
print("Dólares:", moeda(euros, taxa))


largura = float(input("Largura: "))
altura = float(input("Altura: "))
tinta = float(input("Tinta por m²: "))

area, perimetro, quantidade = parede(largura, altura, tinta)

print("Área:", area)
print("Perímetro:", perimetro)
print("Tinta:", quantidade)


preco = float(input("Preço: "))
percentagem = float(input("Desconto (%): "))

valor, final = desconto(preco, percentagem)

print("Desconto:", valor)
print("Preço final:", final)