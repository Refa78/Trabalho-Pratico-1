# Exercício 1
# Verificar nome válido usando try/except

try:
    nome = input("Digite um nome: ")

    if nome.strip() == "":
        raise ValueError("Nome inválido!")

    print("Nome válido:", nome)

except ValueError as erro:
    print("Erro:", erro)