# Funções - DEF

1. Faça um programa contendo funções que recebam:
- Um número inteiro e que retorne o dobro deste número
- Dois números inteiros e que retorne o maior entre eles
- Um número inteiro e que retorne o valor do fatorial deste número
- Um número inteiro e positivo, que retorne a soma dos elementos inteiros existentes entre 1 e o número (inclusive)
- Um número inteiro e que retorne True se o número for par, e False caso contrário

```python

def dobrar_numero(numero):
    return numero * 2

def encontrar_maior(numero1, numero2):
    return max(numero1, numero2)

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def somar_elementos(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

def verificar_paridade(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Menu de opções
print("Escolha uma opção:")
print("1. Dobrar número")
print("2. Encontrar o maior entre dois números")
print("3. Calcular o fatorial de um número")
print("4. Somar elementos de 1 até um número")
print("5. Verificar se um número é par")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    numero = int(input("Digite um número inteiro: "))
    resultado = dobrar_numero(numero)
    print("O dobro do número é:", resultado)

elif opcao == 2:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    resultado = encontrar_maior(numero1, numero2)
    print("O maior número é:", resultado)

elif opcao == 3:
    numero = int(input("Digite um número inteiro: "))
    resultado = calcular_fatorial(numero)
    print("O fatorial do número é:", resultado)

elif opcao == 4:
    numero = int(input("Digite um número inteiro e positivo: "))
    resultado = somar_elementos(numero)
    print("A soma dos elementos é:", resultado)

elif opcao == 5:
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_paridade(numero)
    print("O número é par?", resultado)

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
```
