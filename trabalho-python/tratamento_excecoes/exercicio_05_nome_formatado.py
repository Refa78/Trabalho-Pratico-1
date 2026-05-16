# Exercício 5
# Nome formatado com tratamento de exceções

try:
    nome = input("Digite o nome completo: ")

    if nome.strip() == "":
        raise ValueError("Nome inválido!")

    nome_formatado = nome.title()

    arquivo = open("nome_formatado.txt", "w", encoding="utf-8")

    arquivo.write(nome_formatado)

    arquivo.close()

    print("Nome gravado com sucesso!")
    print("Nome formatado:", nome_formatado)

except ValueError as erro:
    print("Erro:", erro)

except FileNotFoundError:
    print("Erro: arquivo não encontrado!")