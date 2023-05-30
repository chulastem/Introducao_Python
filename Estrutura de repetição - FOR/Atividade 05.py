
"""5. Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado."""

numero = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print("A soma dos números inteiros entre 1 e", numero, "é:", soma)
