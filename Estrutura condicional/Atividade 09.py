
"""Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral:
- não eleitor (abaixo de 16 anos);
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)
"""

print("Classe Eleitoral")
idade = int(input("Digite sua idade:"))
if(idade < 16):
  print("Classe: Não Eleitor")
elif(idade >= 18 and idade <= 65):
  print("Classe: Eleitor Obrigatorio")
elif(idade >= 16) or (idade < 18) or (idade > 65):
  print("Classe: Eleitor Facultativo")
