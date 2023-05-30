
"""
2. Crie duas listas com 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma que contenha a soma dos elementos de mesma posição das duas listas originais, e outra que contenha a multiplicação dos valores de mesma posição. Imprima em seguida as 3 listas."""

import random

# Criando duas listas com 10 valores inteiros aleatórios
lista1 = random.sample(range(1, 101), 10)
lista2 = random.sample(range(1, 101), 10)

# Criando a lista com a soma dos elementos de mesma posição
soma_lista = [x + y for x, y in zip(lista1, lista2)]

# Criando a lista com a multiplicação dos valores de mesma posição
multiplicacao_lista = [x * y for x, y in zip(lista1, lista2)]

# Imprimindo as listas originais, a lista com a soma e a lista com a multiplicação
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista com a soma dos valores:", soma_lista)
print("Lista com a multiplicação dos valores:", multiplicacao_lista)
