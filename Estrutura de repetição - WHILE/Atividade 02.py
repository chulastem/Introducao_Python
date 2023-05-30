"""
2. Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos

A leitura será encerrada quando o usuário informar uma idade negativa.
"""

id50 = 0
somaidade = 0
contid = 0
contid40 = 0
idade = 0

print("Digite um valor negativo para sair do prgrama.")

while (idade >= 0):
  idade = int(input("Digite a sua idade:"))
  if idade < 0:
    print("Programa encerrado")
    break
  contid += 1
  somaidade += idade
  if idade >= 50:
    id50 += 1
  elif idade <= 40:
    contid40 += 1

print("total digitado:", contid)
print("Quantidade de pessoas com idade acima de 50 anos:", id50)
print("Media das idades digitadas:", somaidade/contid)
print("Percentual de pessoas com idade abaixo de 40 anos:", contid40/contid*100)
