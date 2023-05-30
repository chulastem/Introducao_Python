"""4. Solicite ao usuário que digite uma palavra. Em seguida, solicite ao mesmo que informe um caractere separador, de maneira que o separador seja incluído na palavra, separando cada letra da palavra digitada."""

# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Solicita ao usuário que informe um caractere separador
caractere = input("Informe um caractere separador: ")

# Separa cada letra da palavra com o caractere separador
palavra_separada = caractere.join(palavra)

# Imprime a palavra separada
print("Palavra separada:", palavra_separada)
