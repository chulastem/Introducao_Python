"""
1. Crie uma lista em python contendo 10 valores inteiros aleatórios, entre 1 e 20. Imprima:
- O maior valor, o menor valor, a soma e a média dos valores na lista
- Ordene a lista, e em seguida, a imprima em ordem crescente
- Imprima a lista em ordem decrescente
- Solicite ao usuário que informe um valor e imprima a quantidade de ocorrências do valor na lista. Imprima uma mensagem, caso o valor não se encontre na lista
"""

import random

# Criando a lista com 10 valores inteiros aleatórios entre 1 e 20
lista = random.sample(range(1, 21), 10)

# Imprimindo a lista original
print("Lista original:", lista)

# a) Encontrando o maior valor, o menor valor, a soma e a média dos valores na lista
maior_valor = max(lista)
menor_valor = min(lista)
soma = sum(lista)
media = soma / len(lista)

print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)
print("Soma dos valores:", soma)
print("Média dos valores:", media)

# b) Ordenando e imprimindo a lista em ordem crescente
lista.sort()
print("Lista em ordem crescente:", lista)

# c) Imprimindo a lista em ordem decrescente
lista.reverse()
print("Lista em ordem decrescente:", lista)

# d) Solicitando ao usuário um valor e contando as ocorrências
valor = int(input("Digite um valor: "))
ocorrencias = lista.count(valor)

if ocorrencias == 0:
    print("O valor não se encontra na lista.")
else:
    print("O valor", valor, "aparece", ocorrencias, "vezes na lista.")