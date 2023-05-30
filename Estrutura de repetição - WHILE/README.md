# Estrutura de repetição - WHILE

1. Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa.
```python
mat = 0 
while (mat >= 0):
  mat = int(input("Digite a matricula do aluno: "))
  if mat < 0:
    print("Programa encerrado")
    break
  nota1 = int(input("Digite a 1ª nota do aluno de 0 - 100: "))
  nota2 = int(input("Digite a 2ª nota do aluno de 0 - 100: "))
  nota3 = int(input("Digite a 3ª nota do aluno de 0 - 100: "))
  media = (nota1+nota2+nota3)/3
  if media >= 70:
    print("Aluno:", mat, "Media =", media," Aprovado!")
  elif media >= 60 and media < 70:
    print("Aluno:", mat, "Media =", media," Exame!")
  elif media < 60:
    print("Aluno:", mat, "Media =", media," Reprovado!")
```
2. Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos

A leitura será encerrada quando o usuário informar uma idade negativa.
```python
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
```
3. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber: 
- A média do salário da população; 
- A média do número de filhos. 

O final da leitura de dados dar-se-á com a entrada de salários negativos. 
```python
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
```
