"""
exercício 08 - Leia nota de um aluno e diga:
Aprovado (>= 10) ou Reprovado (< 10)
"""
while True:
    nota = int(input("Digite a nota: "))
    if nota < 0 or nota > 20:
        print("Nota inválida")
    elif nota >= 10:
        print("Aprovado")
    else:
        print("Reprovado")

    continuar = input("\nDeseja consultar outro aluno (s/n)? ").lower()
    if continuar != 's':
        print("Encerrando o programa...")
        break    