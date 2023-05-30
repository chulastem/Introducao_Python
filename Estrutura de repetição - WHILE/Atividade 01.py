"""
1. Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa.
"""

mat = 0
while (mat >= 0):
  mat = int(input("Digite a matricula do aluno: "))
  if mat < 0:
    print("Programa encerrado")
    break
  nota1 = int(input("Digite a 1ª nota do aluno de 0 - 100: "))
  nota2 = int(input("Digite a 2ª nota do aluno de 0 - 100: "))
  nota3 = int(input("Digite a 3ª nota do aluno de 0 - 100: "))
  media = (nota1+nota2+nota3)/3
  if media >= 70:
    print("Aluno:", mat, "Media =", media," Aprovado!")
  elif media >= 60 and media < 70:
    print("Aluno:", mat, "Media =", media," Exame!")
  elif media < 60:
    print("Aluno:", mat, "Media =", media," Reprovado!")
