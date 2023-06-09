# Estruturas de Dados - Lista

1. Crie uma lista em python contendo 10 valores inteiros aleatórios, entre 1 e 20. Imprima:
- O maior valor, o menor valor, a soma e a média dos valores na lista
- Ordene a lista, e em seguida, a imprima em ordem crescente
- Imprima a lista em ordem decrescente
- Solicite ao usuário que informe um valor e imprima a quantidade de ocorrências do valor na lista. Imprima uma mensagem, caso o valor não se encontre na lista

```python
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
```
2. Crie duas listas com 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma que contenha a soma dos elementos de mesma posição das duas listas originais, e outra que contenha a multiplicação dos valores de mesma posição. Imprima em seguida as 3 listas.
```python

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
```
3. Considere a seguinte lista: [10, 20, 30, 30, 30, 40, 10, 20]
	Faça um programa que exclua todas as ocorrências do número 30 da lista

```python
lista = [10, 20, 30, 30, 30, 40, 10, 20]

while 30 in lista:
    lista.remove(30)

print("Lista sem as ocorrências do número 30:", lista)
```
4. Crie uma lista contendo 10 valores inteiros aleatórios (escolha uma faixa qualquer). Crie outras duas listas: uma para armazenar os valores pares da primeira lista, e outra para armazenar os valores ímpares. Imprima em seguida as 3 listas."""
```python
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
```
5. Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
27/05/2023 – 27 de maio de 2023
- (dica: crie uma lista contendo o nome de cada mês do ano)
```python

# Lista com o nome dos meses
meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

# Solicita ao usuário que digite a data
data = input("Digite uma data no formato DD/MM/AAAA: ")

# Separa o dia, mês e ano da data
dia, mes, ano = data.split('/')

# Converte o dia e o mês para inteiros
dia = int(dia)
mes = int(mes)

# Imprime a data por extenso
data_extenso = f"{dia} de {meses[mes - 1]} de {ano}"
print("Data por extenso:", data_extenso)
```
6. Faça um programa que gere uma lista contendo 6 números aleatórios, de 1 a 60, que serão jogados na Mega-Sena. Em seguida, solicite ao usuário os 6 números sorteados. Imprima a lista contendo os números jogados, e a quantidade de números acertados no sorteio.
```python
import random

# Gerando a lista com 6 números aleatórios de 1 a 60
numeros_jogados = random.sample(range(1, 61), 6)

# Solicitando ao usuário os 6 números sorteados
numeros_sorteados = []
for i in range(6):
    numero = int(input("Digite o {}º número sorteado: ".format(i+1)))
    numeros_sorteados.append(numero)

# Imprimindo a lista de números jogados e a quantidade de acertos
print("Números jogados:", numeros_jogados)

acertos = 0
for numero in numeros_sorteados:
    if numero in numeros_jogados:
        acertos += 1

print("Quantidade de números acertados:", acertos)
```
