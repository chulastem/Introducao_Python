
# Estrutura sequencial

1. Leia três números inteiros e imprima a média aritmética entre esses números.
```python
print("Digite 3 números")
a = float(input())
b = float(input())
c = float(input())
media = (a+b+c)/3
print("A média aritmetica desses 3 valores é " + str(media))
```
2. Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
* A idade da pessoa no ano atual
* A idade que a pessoa terá em 2050

```python
print("Digite o Ano atual:")
ano = int(input())
print("Digite o Ano do seu nascimento")
anonasc = int(input())
idade = ano-anonasc
idade2050 = 2050-anonasc
print("A idade no ano atual é:" + str(idade))
print("A idade em 2050 será:  " + str(idade2050))
```
3. faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação).
```python
import math
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))
delta = b**2 - 4*a*c
x = -b / (2*a)
print("A equação possui uma raiz real:", x)
```
4. Leia um número e imprima a tabuada de multiplicar deste número. 
```python
a = int(input("Digite um número inteiro: "))
print(int(a),"x 01 = ",(int(a)*1))
print(int(a),"x 02 = ",(int(a)*2))
print(int(a),"x 03 = ",(int(a)*3))
print(int(a),"x 04 = ",(int(a)*4))
print(int(a),"x 05 = ",(int(a)*5))
print(int(a),"x 06 = ",(int(a)*6))
print(int(a),"x 07 = ",(int(a)*7))
print(int(a),"x 08 = ",(int(a)*8))
print(int(a),"x 09 = ",(int(a)*9))
print(int(a),"x 10 = ",(int(a)*10))
```
5. Receba um número positivo, calcule e mostre:
* O número digitado ao quadrado
* O número digitado ao cubo
* A raiz quadrada do número digitado
* A raiz cúbica do número digitado.

```python
a = int(input("Digite um número inteiro positivo:"))
print("O numero digitado ao quadrado:", int(a)*int(a))
print("O numeor digitado ao cubo:", int(a)*int(a)*int(a))
print("Raiz quadrada do numero digitado:", int(a)/2)
print("Raiz cubica do numero digitado:", int(a)/3)
```
6. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom. Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta."""
```python
a = float(input("Valor gasto R$:"))
gorj = a * 0.10
print("10% do garçom = R$", gorj)
```
7. Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado. """
```Python
a = int(input("Digite um numero inteiro:"))
print("Antecessor:", a-1)
print("Sucessor:", a+1)
print("Dobro:", a*2)
print("Metade", a/2)
```
8. Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
* Peso ideal (P) = (72,7 * H) – 58. 
```python
h = float(input("Digite a sua altura"))
p = (72.7*h)-58
print("Peso ideal =", p)
```
9. Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido. 
* Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
```python
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = b
b = a
a = c
print("Valor de a:", a)
print("Valor de b:", b)
```
10. Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato. Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.

```python
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_candidato1 = int(input("Digite o número de votos do primeiro candidato: "))
votos_candidato2 = int(input("Digite o número de votos do segundo candidato: "))

percentual_candidato1 = (votos_candidato1 / total_eleitores) * 100
percentual_candidato2 = (votos_candidato2 / total_eleitores) * 100
percentual_nulos = 100 - (percentual_candidato1 + percentual_candidato2)

print("Percentual de votos do primeiro candidato: {:.2f}%".format(percentual_candidato1))
print("Percentual de votos do segundo candidato: {:.2f}%".format(percentual_candidato2))
print("Percentual de votos nulos: {:.2f}%".format(percentual_nulos))
```
