"""6. Faça um programa que gere uma lista contendo 6 números aleatórios, de 1 a 60, que serão jogados na Mega-Sena. Em seguida, solicite ao usuário os 6 números sorteados. Imprima a lista contendo os números jogados, e a quantidade de números acertados no sorteio."""

import random

# Gerando a lista com 6 números aleatórios de 1 a 60
numeros_jogados = random.sample(range(1, 61), 6)

# Solicitando ao usuário os 6 números sorteados
numeros_sorteados = []
for i in range(6):
    numero = int(input("Digite o {}º número sorteado: ".format(i+1)))
    numeros_sorteados.append(numero)

# Imprimindo a lista de números jogados e a quantidade de acertos
print("Números jogados:", numeros_jogados)

acertos = 0
for numero in numeros_sorteados:
    if numero in numeros_jogados:
        acertos += 1

print("Quantidade de números acertados:", acertos)