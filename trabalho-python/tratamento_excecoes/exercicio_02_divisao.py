# Exercício 2
# Divisão com tratamento de exceções

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = numero1 / numero2

    print("Resultado da divisão:", resultado)

except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida!")

except ValueError:
    print("Erro: você deve digitar apenas números inteiros!")