"""
Exercício 6 - Concatenação reversa
Enunciado: ados os ficheiros fich3.txt e fich4.txt, crie uma função que receba os nomes desses ficheiros e gere um novo ficheiro chamado final.txt. Este novo ficheiro deve conter o conteúdo do fich3 na ordem normal, seguido pelo conteúdo do fich4 invertido (da última linha para a primeira).
Exemplo:  Fich3: 		    Fich4:		 	            Final:
          Olá mundo. 	  Amanhã fará sol. 	      Olá mundo.
          Hoje chove.   Está um frio danado. 	  Hoje chove.
					                                      Está um frio danado.
					                                      Amanhã fará sol.
"""
def concatenacao_reversa(fich_a, fich_b, nome_saida):
    try:
        # 1. Ler o conteúdo do fich3
        with open(fich_a, "r", encoding="utf-8") as f1:
            linhas1 = f1.readlines()

        # 2. Ler o conteúdo do fich4
        with open(fich_b, "r", encoding="utf-8") as f2:
            linhas2 = f2.readlines()

        # 3. Inverter a ordem das linhas do segundo ficheiro (fich4)
        linhas2_reversas = linhas2[::-1]

        # 4. Criar o ficheiro final.txt
        with open(nome_saida, "w", encoding="utf-8") as ff:
            ff.writelines(linhas1)
            
            # Pequeno ajuste: garante que o fich4 começa numa nova linha
            if linhas1 and not linhas1[-1].endswith('\n'):
                ff.write('\n')
                
            ff.writelines(linhas2_reversas)

        print(f"Sucesso! O ficheiro '{nome_saida}' foi gerado com a reversão do '{fich_b}'.")

    except FileNotFoundError:
        print("Erro: Certifique-se que 'fich3.txt' e 'fich4.txt' existem na pasta.")

# Chamada da função com os seus ficheiros novos
concatenacao_reversa("fich3.txt", "fich4.txt", "final.txt")
