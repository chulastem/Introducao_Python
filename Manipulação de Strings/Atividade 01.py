
"""
1. Solicite ao usuário que digite uma frase. Imprima:
	- o tamanho (em caracteres) da frase
	- a frase toda em maiúscula
	- a frase toda em minúscula
	- a frase na vertical(letra por letra)
	- solicite ao usuário que informe uma posição inicial e final na frase, e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	- a frase em ordem inversa
	- solicite ao usuário que informe duas palavras. Substitua, na frase informada, a primeira palavra informada pelo usuário, pela segunda palavra informada. Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.
em pyhton
"""

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
