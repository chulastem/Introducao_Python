"""Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação)."""

import math
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))
delta = b**2 - 4*a*c
x = -b / (2*a)
print("A equação possui uma raiz real:", x)
