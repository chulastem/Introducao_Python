
"""Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido.
* Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
"""

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = b
b = a
a = c
print("Valor de a:", a)
print("Valor de b:", b)
