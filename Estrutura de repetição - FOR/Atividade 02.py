
"""2. Faça um programa que leia um número e que imprima os números ímpares de 1 até o número informado. """

numero = int(input("Digite um número: "))
print("Números ímpares de 1 até", numero, ":")

for i in range(1, numero + 1, 2):
    print(i)
