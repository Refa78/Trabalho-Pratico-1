# Exercício 1
# Cadeia de DNA inversa

arquivo = open("dna.txt", "r", encoding="utf-8")

dna = arquivo.read().strip()

arquivo.close()

dna_inverso = dna[::-1]

print("DNA original:", dna)
print("DNA inverso:", dna_inverso)