"""Faça um programa que receba a idade de um nadador e mostre a sua categoria

* até 7 anos
INFANTIL
* 8 a 10 anos
JUVENIL
* 11 a 15 anos
ADOLESCENTE
* 16 a 30 anos
ADULTO
* acima de 30 anos
SENIOR
"""

print("Categoria")
idade = int(input("Digite a idade do nadador:"))
if(idade <= 7):
  print("Categoria: INFANTIL")
elif(idade >= 8 and idade <= 10):
  print("Categoria: JUVENIL")
elif(idade >= 11 and idade <= 15):
  print("Categoria: ADOLESCENTE")
elif(idade >= 16 and idade <= 30):
  print("Categoria: ADULTO")
elif(idade > 30):
  print("Categoria: SENIOR")
