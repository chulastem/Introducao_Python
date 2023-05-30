
"""Faça um programa que solicite ao usuário que informe dois números e que exiba o seguinte menu:
1. – Somar
2. – Subtrair
3. – Multiplicar
4. – Dividir
5. – Sair
Em seguida, leia a opção escolhida e exiba o resultado de acordo com a opção.
"""

a = float(input("Digite o 1º valor:"))
b = float(input("Digite o 2º valor:"))
print("O que deseja fazer com os valores digitados?")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Sair")
opcao = int(input("Digite a opção solicitada:"))

if(opcao == 1):
  print("A soma dos valor é: ", a+b)
elif(opcao == 2):
  print("A subtração dos valores é: ", a-b)
elif(opcao == 3):
  print("A multiplicação dos valores é: ", a*b)
elif(opcao == 4):
  print("A divisão dos valores é: ", a/2)
elif(opcao == 5):
  print("Fim do programa")
else:
  print("Opção invalida! Programa encerrado")
