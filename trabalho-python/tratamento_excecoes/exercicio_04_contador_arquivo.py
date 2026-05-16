# Exercício 4
# Contar palavras e linhas com tratamento de exceções

try:
    arquivo = open("texto.txt", "r", encoding="utf-8")

    linhas = arquivo.readlines()

    quantidade_linhas = len(linhas)

    quantidade_palavras = 0

    for linha in linhas:
        palavras = linha.split()
        quantidade_palavras += len(palavras)

    arquivo.close()

    print("Quantidade de linhas:", quantidade_linhas)
    print("Quantidade de palavras:", quantidade_palavras)

except FileNotFoundError:
    print("Erro: arquivo não encontrado no diretório!")