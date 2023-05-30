# Manipulação de Strings

1. Solicite ao usuário que digite uma frase. Imprima:
	- o tamanho (em caracteres) da frase
	- a frase toda em maiúscula
	- a frase toda em minúscula
	- a frase na vertical(letra por letra)
	- solicite ao usuário que informe uma posição inicial e final na frase, e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	- a frase em ordem inversa
	- solicite ao usuário que informe duas palavras. Substitua, na frase informada, a primeira palavra informada pelo usuário, pela segunda palavra informada. Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.
em pyhton
```python

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Tamanho da frase
tamanho = len(frase)
print("Tamanho da frase:", tamanho)

# Frase em maiúscula
maiuscula = frase.upper()
print("Frase em maiúscula:", maiuscula)

# Frase em minúscula
minuscula = frase.lower()
print("Frase em minúscula:", minuscula)

# Frase na vertical (letra por letra)
print("Frase na vertical:")
for letra in frase:
    print(letra)

# Solicita ao usuário as posições inicial e final
inicio = int(input("Informe a posição inicial: "))
fim = int(input("Informe a posição final: "))

# Parte da frase dentro das posições informadas
parte = frase[inicio:fim]
print("Parte da frase:", parte)

# Frase em ordem inversa
inversa = frase[::-1]
print("Frase em ordem inversa:", inversa)

# Solicita ao usuário duas palavras para substituição
palavra1 = input("Informe a primeira palavra: ")
palavra2 = input("Informe a segunda palavra: ")

# Substitui a primeira palavra pela segunda palavra na frase
nova_frase = frase.replace(palavra1, palavra2)
print("Nova frase:", nova_frase)
```
2. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que digite uma palavra. Imprima uma mensagem informando a quantidade de vezes em que a palavra se encontra na frase (considere que a palavra pode estar em maiúscula ou minúscula na frase).

```python
# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Converte a frase e a palavra para minúsculas para fazer a comparação
frase_min = frase.lower()
palavra_min = palavra.lower()

# Conta a quantidade de vezes que a palavra aparece na frase
quantidade = frase_min.count(palavra_min)

# Imprime a quantidade de vezes que a palavra aparece na frase
print("A palavra", palavra, "aparece", quantidade, "vezes na frase.")
```
3. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que informe um caractere de maneira que a frase seja dividida em partes de acordo com o caractere informado. Imprima na tela a frase dividida.
```python

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário que informe um caractere para divisão
caractere = input("Informe um caractere para divisão: ")

# Divide a frase em partes de acordo com o caractere informado
partes = frase.split(caractere)

# Imprime as partes da frase
print("Frase dividida:")
for parte in partes:
    print(parte)
```
4. Solicite ao usuário que digite uma palavra. Em seguida, solicite ao mesmo que informe um caractere separador, de maneira que o separador seja incluído na palavra, separando cada letra da palavra digitada.
```python
# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Solicita ao usuário que informe um caractere separador
caractere = input("Informe um caractere separador: ")

# Separa cada letra da palavra com o caractere separador
palavra_separada = caractere.join(palavra)

# Imprime a palavra separada
print("Palavra separada:", palavra_separada)
```
5. Solicite ao usuário que digite uma palavra e imprima uma mensagem informando se a palavra é ou não um palíndromo (uma palavra que se lê da mesma maneira nos dois sentidos. Por exemplo: OVO, RADAR, OSSO etc.)
```python
# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
```
