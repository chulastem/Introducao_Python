"""Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
MÉDIA
MENSAGEM
* (>= 0 e < 3
REPROVADO)
* (>= 3 e < 7
EXAME)
* (>= 7 e <= 10
APROVADO)
"""

nota1 = int(input("Digite a 1º nota do aluno (0-10):"))
nota2 = int(input("Digite a 2º nota do aluno (0-10):"))
nota3 = int(input("Digite a 3º nota do aluno (0-10):"))
media = (nota1 + nota2 + nota3)/3
if(media >= 0 and media <3):
  print("REPROVADO")
elif(media >= 3 and media < 7):
  print("EXAME")
elif(media >= 7 and media <= 10):
  print("APROVADO")