"""Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados."""

print("verificar se os valores podem ser os comprimentos dos lados de um triângulo")
x = float(input("Digite o valor de X"))
y = float(input("Digite o valor de Y"))
z = float(input("Digite o valor de Z"))
if(z < x + y and x < y + z and y < z + x):
  print("Os valores podem formar um triângulo")
else:
  print("Os valores NÃO formam um triângulo")