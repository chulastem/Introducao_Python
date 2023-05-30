
"""Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número."""

print("Mês do ano")
mes = int(input("Digite um numero de 1 a 12:"))
if(mes == 1):
  print("JANEIRO")
elif(mes == 2):
  print("FEVEREIRO")
elif(mes == 3):
  print("MARÇO")
elif(mes == 4):
  print("ABRIL")
elif(mes == 5):
  print("MAIO")
elif(mes == 6):
  print("JUNHO")
elif(mes == 7):
  print =("JULHO")
elif(mes == 8):
  print("AGOSTO")
elif(mes == 9):
  print("SETEMBRO")
elif(mes == 10):
  print("OUTUBRO")
elif(mes == 11):
  print("NOVEMBRO")
elif(mes == 12):
  print("DEZEMBRO")
else:
  print("Nº invalido - Não existe mês com esse número")