"""
Faça um programa que receba dois números e mostre o maior e o menor. Emita uma mensagem, caso os dois sejam iguais.
"""

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
if(a>b):
  print(a,"é maior que ", b)
elif(b>a):
  print(b,"é maior que ", a)
elif(a==b):
  print("Os dois valores são iguais")