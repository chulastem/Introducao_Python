
# Estrutura de repetição - FOR  

1. Faça um programa que faça a leitura de 5 valores, e para cada valor, mostre o seu dobro na tela.
```python
for i in range(0,5):
  n = int(input("Digite um valor númerico: "))
  print("O dobro do valor é =", n*2)
```
2. Faça um programa que leia um número e que imprima os números ímpares de 1 até o número informado.
```python
numero = int(input("Digite um número: "))
print("Números ímpares de 1 até", numero, ":")

for i in range(1, numero + 1, 2):
    print(i)
```
3. Leia um número e imprima a tabuada de multiplicar deste número.
```python
numero = int(input("Digite um número: "))
for i in range(1,11):
  print(numero, "x", i, "=",numero*i)
```
4. Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados.
```python
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print("Números inteiros entre", menor, "e", maior, ":")

for numero in range(menor + 1, maior):
    print(numero)
```
5. Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado.
```python
numero = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print("A soma dos números inteiros entre 1 e", numero, "é:", soma)
```
6. Faça um programa que leia um número e que calcule o fatorial deste número.
```python
numero = int(input("Digite um número inteiro: "))
for i in range (1,numero):
 numero *= i
print("Fotorial do numero é:", numero)
```
7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos.
```python
somapesos = 0
for i in range (10):
  peso = int(input("Digite sem peso em kg:"))
  somapesos += peso
media = somapesos/10
print("Média dos pesos digitados:",media)
```
8. Faça um programa que leia o sexo e o peso de 10 pessoas, e mostre quantas pessoas do sexo masculino possuem peso entre 60 e 80 kg, bem como a quantidade de mulheres que possuem peso entre 50 e 70 kg.
```python
somapeso1 = 0
somapeso2 = 0 

for i in range (10):
  sexo = int(input("Qual o seu sexo? (M = 1, F = 2):"))
  peso = int(input("Digite seu peso em kg:"))
  if sexo == 1 and peso >= 60 and peso <=80:
    somapeso1 += 1
  elif sexo == 2 and peso >= 50 and peso <= 70:
    somapeso2 += 1 

print("total do sexo MASCULINO com peso entre 60 a 80: ",somapeso1)
print("total do sexo FEMININO com peso entre 50 a 70: ",somapeso2)
```
