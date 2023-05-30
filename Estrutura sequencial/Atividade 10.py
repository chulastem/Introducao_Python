"""Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato. Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.
"""

total_eleitores = int(input("Digite o número total de eleitores: "))
votos_candidato1 = int(input("Digite o número de votos do primeiro candidato: "))
votos_candidato2 = int(input("Digite o número de votos do segundo candidato: "))

percentual_candidato1 = (votos_candidato1 / total_eleitores) * 100
percentual_candidato2 = (votos_candidato2 / total_eleitores) * 100
percentual_nulos = 100 - (percentual_candidato1 + percentual_candidato2)

print("Percentual de votos do primeiro candidato: {:.2f}%".format(percentual_candidato1))
print("Percentual de votos do segundo candidato: {:.2f}%".format(percentual_candidato2))
print("Percentual de votos nulos: {:.2f}%".format(percentual_nulos))
