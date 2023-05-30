
"""7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos."""

somapesos = 0
for i in range (10):
  peso = int(input("Digite sem peso em kg:"))
  somapesos += peso
media = somapesos/10
print("Média dos pesos digitados:",media)
