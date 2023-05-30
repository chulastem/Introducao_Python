
"""Faça um programa que leia um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número."""

print("Dia da semana")
dia = int(input("Digite um numero de 1 a 7:"))
if(dia == 1):
  print("DOMINGO")
elif(dia == 2):
  print("SEGUNDA-FEIRA")
elif(dia == 3):
  print("TERÇA-FEIRA")
elif(dia == 4):
  print("QUARTA-FEIRA")
elif(dia == 5):
  print("QUINTA-FEIRA")
elif(dia == 6):
  print("SEXTA-FEIRA")
elif(dia == 7):
  print =("SABADO")
else:
  print("Nº invalido - Não existe dia da semana com esse número")
