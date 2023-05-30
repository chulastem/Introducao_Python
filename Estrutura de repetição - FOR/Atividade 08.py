"""8. Faça um programa que leia o sexo e o peso de 10 pessoas, e mostre quantas pessoas do sexo masculino possuem peso entre 60 e 80 kg, bem como a quantidade de mulheres que possuem peso entre 50 e 70 kg."""

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