import os

# Lista de pastas para as Fichas do CINEL
pastas = ['ficha_01', 'ficha_02', 'ficha_03']

for nome in pastas:
    if not os.path.exists(nome):
        os.mkdir(nome)
        print(f"✅ Pasta '{nome}' criada com sucesso!")
    else:
        print(f"⚠️ A pasta '{nome}' já existe.")