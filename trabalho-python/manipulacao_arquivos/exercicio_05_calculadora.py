# Exercício 5
# Mini calculadora com arquivo txt

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

arquivo = open("resultado_calculadora.txt", "w", encoding="utf-8")

arquivo.write(f"Número 1: {numero1}\n")
arquivo.write(f"Número 2: {numero2}\n\n")

arquivo.write(f"Soma: {soma}\n")
arquivo.write(f"Subtração: {subtracao}\n")
arquivo.write(f"Multiplicação: {multiplicacao}\n")
arquivo.write(f"Divisão: {divisao}\n")

arquivo.close()

print("Resultados gravados com sucesso!")