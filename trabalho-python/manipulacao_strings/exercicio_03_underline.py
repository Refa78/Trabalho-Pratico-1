# Exercício 3
# Substituir espaços por underline

arquivo = open("texto_underline.txt", "r", encoding="utf-8")

texto = arquivo.read()

arquivo.close()

texto_modificado = texto.replace(" ", "_")

print("Texto original:")
print(texto)

print("\nTexto modificado:")
print(texto_modificado)