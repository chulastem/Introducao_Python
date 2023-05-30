"""Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
1.   A idade da pessoa no ano atual
2.   A idade que a pessoa terá em 2050
"""

print("Digite o Ano atual:")
ano = int(input())
print("Digite o Ano do seu nascimento")
anonasc = int(input())
idade = ano-anonasc
idade2050 = 2050-anonasc
print("A idade no ano atual é:" + str(idade))
print("A idade em 2050 será:  " + str(idade2050))
