# Exercício 2
# Cadastro de pessoa em arquivo txt

from datetime import datetime

nome = input("Digite o nome: ")
rg = input("Digite o RG: ")
cpf = input("Digite o CPF: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

arquivo = open("dados_pessoa.txt", "w", encoding="utf-8")

arquivo.write(f"Nome: {nome}\n")
arquivo.write(f"RG: {rg}\n")
arquivo.write(f"CPF: {cpf}\n")
arquivo.write(f"Ano de nascimento: {ano_nascimento}\n")
arquivo.write(f"Idade: {idade} anos\n")

arquivo.close()

print("Dados gravados com sucesso!")