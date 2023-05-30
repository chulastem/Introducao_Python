""" Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação:
*  => 7 -> Aprovado
* < 7 -> Reprovado
"""

nota1 = int(input("Digite a 1º nota do aluno (0-10):"))
nota2 = int(input("Digite a 2º nota do aluno (0-10):"))
media = (nota1 + nota2)/2
if(media >= 7):
  print("APROVADO")
elif(media < 7):
  print("REPROVADO")
