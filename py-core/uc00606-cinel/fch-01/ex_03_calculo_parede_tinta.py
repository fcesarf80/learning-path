"""
Exercício 03 - Calculo parede tinta
Enunciado: A Joana pretende fazer um grafitti numa parede. Para tal, terá de a preparar.
Assim, ajude a Joana, desenvolvendo um programa onde esta somente terá de inserir a altura,
largura da área que pretende preparar e ainda a quantidade de tinta que irá gastar por metro quadrado.
O programa deverá devolver:
"""
larg = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))

#a. Área a pintar;
area = larg * alt
print(f"A parede tem {area:.1f} de metros quadrados")

#b. Perímetro;
perim = (2 * alt) + (2 * larg)
print(f"O perimetro da parede é {perim:.1f} de metros")

#c. Qnt de tinta que irá gastar no total da preparação da parede.
tint_media = float(input("Joana, qt gastas em média por "
                         "metro quadrado pintado? "))
#1m    -- tint_media
#area  --  X litros
x = area * tint_media
print(f"A Joana vai gastar em média {x} litros de tinta")