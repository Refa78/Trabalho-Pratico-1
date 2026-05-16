# Exercício 3
# Fatorial com tratamento de exceções

import math

lista = [5, 3, -1, "python", 4]

for elemento in lista:

    try:
        if not isinstance(elemento, int):
            raise TypeError("Elemento não é número inteiro!")

        if elemento < 0:
            raise ValueError("Número negativo não possui fatorial!")

        resultado = math.factorial(elemento)

        print(f"Fatorial de {elemento} = {resultado}")

    except TypeError as erro:
        print("Erro:", erro)

    except ValueError as erro:
        print("Erro:", erro)
        