
"""4. Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados."""

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print("Números inteiros entre", menor, "e", maior, ":")

for numero in range(menor + 1, maior):
    print(numero)
