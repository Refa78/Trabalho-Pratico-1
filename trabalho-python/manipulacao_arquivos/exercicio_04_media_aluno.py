# Exercício 4
# Média do aluno e situação final

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

arquivo = open("resultado_aluno.txt", "w", encoding="utf-8")

arquivo.write(f"Nome: {nome}\n")
arquivo.write(f"Média Final: {media:.2f}\n")
arquivo.write(f"Situação: {situacao}\n")

arquivo.close()

print("Resultado gravado com sucesso!")