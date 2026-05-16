# Exercício 4
# Lista sem palavras repetidas

arquivo = open("frase.txt", "r", encoding="utf-8")

frase = arquivo.read()

arquivo.close()

palavras = frase.split()

lista_sem_repeticao = []

for palavra in palavras:
    if palavra not in lista_sem_repeticao:
        lista_sem_repeticao.append(palavra)

print("Lista sem repetição:")
print(lista_sem_repeticao)