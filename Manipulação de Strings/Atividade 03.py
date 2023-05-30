
"""3. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que informe um caractere de maneira que a frase seja dividida em partes de acordo com o caractere informado. Imprima na tela a frase dividida.

"""

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
