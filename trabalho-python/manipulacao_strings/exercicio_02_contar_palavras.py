# Exercício 2
# Contar palavras de um arquivo txt

arquivo = open("texto_palavras.txt", "r", encoding="utf-8")

texto = arquivo.read()

arquivo.close()

palavras = texto.split()

quantidade = len(palavras)

print("Quantidade de palavras:", quantidade)