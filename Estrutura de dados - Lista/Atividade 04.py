
"""4. Crie uma lista contendo 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma para armazenar os valores pares da primeira lista, e outra para armazenar os valores ímpares. Imprima em seguida as 3 listas."""

import random

# Criando uma lista com 10 valores inteiros aleatórios
lista = random.sample(range(1, 101), 10)

# Criando as listas para armazenar os valores pares e ímpares
pares = []
impares = []

# Separando os valores pares e ímpares da lista original
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Imprimindo as listas original, de pares e de ímpares
print("Lista original:", lista)
print("Valores pares:", pares)
print("Valores ímpares:", impares)

