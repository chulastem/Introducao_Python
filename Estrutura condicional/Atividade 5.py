"""Faça um programa que leia o sexo e a altura (H - em metros) de uma pessoa, calcule e apresente seu peso ideal utilizando as seguintes fórmulas:
* Peso ideal (homens) = (72,7 * H) – 58.
* Peso ideal (mulheres) = (62,1 * H) – 44,7

Sugestão: para identificar o sexo da pessoa, solicite ao usuário que informe 1 para homens, e 2 para mulheres
"""

sexo = int(input("Digite seu sexo (H=1)(F=2):"))
altura = float(input("Digite sua altura:"))
if (sexo == 1):
  pesoid = (72.7*altura)-58
  print("Seu peso ideal é ", pesoid)
elif (sexo == 2):
  pesoid = (62.1*altura)-44.7
  print("Seu peso ideal é ", pesoid)
