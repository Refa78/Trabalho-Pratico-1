# Exercício 3
# Ler linhas de um arquivo e armazenar em uma lista

arquivo = open("linhas.txt", "r", encoding="utf-8")

linhas = []

for linha in arquivo:
    linhas.append(linha.strip())

arquivo.close()

print("Lista de linhas:")
print(linhas)