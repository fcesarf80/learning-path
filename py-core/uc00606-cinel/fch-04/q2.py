"""
2) Suponha que a classificação de um aluno é determinada em função da sua nota, que deve ser um valor inteiro entre 0 a 20, conforme a seguinte informação: Se a nota for entre 0 a 9 classificação = a	insuficiente, se entre 10 a 18 = Bom e entre 19 a 20 = Muito Bom. No fim a mensagem terá que usar o nome, a nota e a classificação.
"""

nome = input("Nome aluno: ")
nota = int(input("Nota (0 a 20):  "))
while nota < 0 or nota > 20:
    nota = int(input("Digite um valor entre 0 e 20:"))
if nota <= 9:
    classi = "Insuficiente"
elif nota <= 18:
    classi = "Bom"
else:
    classi = "Muito Bom"
print(f"Nome: {nome}", "\nNota: {nota}")
print(f"Classificação: {classi}")