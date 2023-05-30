
"""2. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que digite uma palavra. Imprima uma mensagem informando a quantidade de vezes em que a palavra se encontra na frase (considere que a palavra pode estar em maiúscula ou minúscula na frase).

"""

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
