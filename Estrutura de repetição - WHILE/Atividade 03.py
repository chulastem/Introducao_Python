
"""3. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:
- A média do salário da população;
- A média do número de filhos.

O final da leitura de dados dar-se-á com a entrada de salários negativos.

"""

filhos = 0
cidadao = 0
salario = 0
while(salario >= 0):
  salario = float(input("Qual o seu salário?:"))
  if salario < 0:
    print("Programa encerrado")
    break

  salario += salario
  cidadao += 1
  filhos = int(input("Quantos filhos você tem?:"))
  filhos += filhos

print("Média do salário da população:", salario/cidadao)
print("Média do número de filhos:", filhos/cidadao)