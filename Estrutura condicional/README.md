# Estrutura condicional

1. Faça um programa que receba dois números e mostre o maior e o menor. Emita uma mensagem, caso os dois sejam iguais.
```python
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
if(a>b):
  print(a,"é maior que ", b)
elif(b>a):
  print(b,"é maior que ", a)
elif(a==b):
  print("Os dois valores são iguais")
```
2. Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
*  => 7 -> Aprovado
* < 7 -> Reprovado
```python
nota1 = int(input("Digite a 1º nota do aluno (0-10):"))
nota2 = int(input("Digite a 2º nota do aluno (0-10):"))
media = (nota1 + nota2)/2
if(media >= 7):
  print("APROVADO")
elif(media < 7):
  print("REPROVADO")
```
3. Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
MÉDIA MENSAGEM
* (>= 0 e < 3 REPROVADO) 
* (>= 3 e < 7 EXAME) 
* (>= 7 e <= 10 APROVADO) 
```python
nota1 = int(input("Digite a 1º nota do aluno (0-10):"))
nota2 = int(input("Digite a 2º nota do aluno (0-10):"))
nota3 = int(input("Digite a 3º nota do aluno (0-10):"))
media = (nota1 + nota2 + nota3)/3
if(media >= 0 and media <3):
  print("REPROVADO")
elif(media >= 3 and media < 7):
  print("EXAME")
elif(media >= 7 and media <= 10):
  print("APROVADO")
```
4. Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
```python
print("verificar se os valores podem ser os comprimentos dos lados de um triângulo")
x = float(input("Digite o valor de X"))
y = float(input("Digite o valor de Y"))
z = float(input("Digite o valor de Z"))
if(z < x + y and x < y + z and y < z + x):
  print("Os valores podem formar um triângulo")
else:
  print("Os valores NÃO formam um triângulo")
```
5. Faça um programa que leia o sexo e a altura (H - em metros) de uma pessoa, calcule e apresente seu peso ideal utilizando as seguintes fórmulas: 
* Peso ideal (homens) = (72,7 * H) – 58. 
* Peso ideal (mulheres) = (62,1 * H) – 44,7

Sugestão: para identificar o sexo da pessoa, solicite ao usuário que informe 1 para homens, e 2 para mulheres
```python
sexo = int(input("Digite seu sexo (H=1)(F=2):"))
altura = float(input("Digite sua altura:"))
if (sexo == 1):
  pesoid = (72.7*altura)-58
  print("Seu peso ideal é ", pesoid)
elif (sexo == 2):
  pesoid = (62.1*altura)-44.7
  print("Seu peso ideal é ", pesoid)
```
6. Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
* IMC= PESO/ALTURA2

e, a situação do peso é determinada pela tabela abaixo:

* IMC abaixo de 20 Abaixo do peso
* IMC de 20 até 25 Peso Normal
* IMC de 25 até 30 Sobre Peso
* IMC de 30 até 40 Obeso
* IMC de 40 e acima Obeso Mórbido
```python
print("Caucular IMC")
peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em METROS:"))
imc = peso / (altura * altura)
if imc < 20:
    print("ABAIXO DO PESO")
elif 20 <= imc < 25:
    print("PESO NORMAL")
elif 25 <= imc < 30:
    print("SOBRE PESO")
elif 30 <= imc < 40:
    print("OBESO")
else:
    print("OBESO MORBIDO")
```
7. Faça um programa que receba a idade de um nadador e mostre a sua categoria

* até 7 anos INFANTIL
* 8 a 10 anos JUVENIL
* 11 a 15 anos ADOLESCENTE
* 16 a 30 anos ADULTO
* acima de 30 anos SENIOR
```python
print("Categoria")
idade = int(input("Digite a idade do nadador:"))
if(idade <= 7):
  print("Categoria: INFANTIL")
elif(idade >= 8 and idade <= 10):
  print("Categoria: JUVENIL")
elif(idade >= 11 and idade <= 15):
  print("Categoria: ADOLESCENTE")
elif(idade >= 16 and idade <= 30):
  print("Categoria: ADULTO")
elif(idade > 30):
  print("Categoria: SENIOR")
```
8. Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
- não eleitor (abaixo de 16 anos); 
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos); 
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)
```python
print("Classe Eleitoral")
idade = int(input("Digite sua idade:"))
if(idade < 16):
  print("Classe: Não Eleitor")
elif(idade >= 18 and idade <= 65):
  print("Classe: Eleitor Obrigatorio")
elif(idade >= 16) or (idade < 18) or (idade > 65):
  print("Classe: Eleitor Facultativo")
```
9. Faça um programa que leia um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número.
```python
print("Dia da semana")
dia = int(input("Digite um numero de 1 a 7:"))
if(dia == 1):
  print("DOMINGO")
elif(dia == 2):
  print("SEGUNDA-FEIRA")
elif(dia == 3):
  print("TERÇA-FEIRA")
elif(dia == 4):
  print("QUARTA-FEIRA")
elif(dia == 5):
  print("QUINTA-FEIRA")
elif(dia == 6):
  print("SEXTA-FEIRA")
elif(dia == 7):
  print =("SABADO")
else:
  print("Nº invalido - Não existe dia da semana com esse número")
```
10. Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.
```python
print("Mês do ano")
mes = int(input("Digite um numero de 1 a 12:"))
if(mes == 1):
  print("JANEIRO")
elif(mes == 2):
  print("FEVEREIRO")
elif(mes == 3):
  print("MARÇO")
elif(mes == 4):
  print("ABRIL")
elif(mes == 5):
  print("MAIO")
elif(mes == 6):
  print("JUNHO")
elif(mes == 7):
  print =("JULHO")
elif(mes == 8):
  print("AGOSTO")
elif(mes == 9):
  print("SETEMBRO")
elif(mes == 10):
  print("OUTUBRO")
elif(mes == 11):
  print("NOVEMBRO")
elif(mes == 12):
  print("DEZEMBRO")
else:
  print("Nº invalido - Não existe mês com esse número")
```
11. Faça um programa que solicite ao usuário que informe dois números e que exiba o seguinte menu:
1. – Somar
2. – Subtrair 
3. – Multiplicar
4. – Dividir
5. – Sair
Em seguida, leia a opção escolhida e exiba o resultado de acordo com a opção.
```python
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
 ```
