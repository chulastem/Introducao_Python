
"""5. Solicite ao usuário que digite uma palavra e imprima uma mensagem informando se a palavra é ou não um palíndromo (uma palavra que se lê da mesma maneira nos dois sentidos. Por exemplo: OVO, RADAR, OSSO etc.)"""

# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")