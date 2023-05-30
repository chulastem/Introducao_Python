"""5. Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
27/05/2023 – 27 de maio de 2023
- (dica: crie uma lista contendo o nome de cada mês do ano)

"""

# Lista com o nome dos meses
meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

# Solicita ao usuário que digite a data
data = input("Digite uma data no formato DD/MM/AAAA: ")

# Separa o dia, mês e ano da data
dia, mes, ano = data.split('/')

# Converte o dia e o mês para inteiros
dia = int(dia)
mes = int(mes)

# Imprime a data por extenso
data_extenso = f"{dia} de {meses[mes - 1]} de {ano}"
print("Data por extenso:", data_extenso)
