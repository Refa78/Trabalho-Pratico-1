# Exercício 1
# Tabuada de multiplicação de 9 em arquivo txt

arquivo = open("tabuada_9.txt", "w", encoding="utf-8")

for i in range(1, 11):
    resultado = 9 * i
    arquivo.write(f"9 x {i} = {resultado}\n")

arquivo.close()

print("Tabuada criada com sucesso!")