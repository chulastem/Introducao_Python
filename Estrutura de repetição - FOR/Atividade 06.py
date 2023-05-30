"""6. Faça um programa que leia um número e que calcule o fatorial deste número."""

numero = int(input("Digite um número inteiro: "))
for i in range (1,numero):
 numero *= i
print("Fotorial do numero é:", numero)
