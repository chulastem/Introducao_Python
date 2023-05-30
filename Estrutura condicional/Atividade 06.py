"""
Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
* IMC= PESO/ALTURA2

e, a situação do peso é determinada pela tabela abaixo:

* IMC abaixo de 20
Abaixo do peso
* IMC de 20 até 25
 Peso Normal
* IMC de 25 até 30
Sobre Peso
* IMC de 30 até 40
Obeso
* IMC de 40 e acima
Obeso Mórbido
"""

print("Caucular IMC")
peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em METROS:"))
imc = peso/(altura*altura)
if(imc < 20):
  print("ABAIXO DO PESO")
elif(imc >= 20 and imc < 25):
  print("PESO NORMAL")
elif(imc >= 25 and imc < 30):
  print("SOBRE PESO")
elif(imc >= 30 and imc < 40):
  print("OBESO")
elif(imc >= 40):
  print("OBESO MORBIDO")