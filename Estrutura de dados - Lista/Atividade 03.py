"""3. Considere a seguinte lista: [10, 20, 30, 30, 30, 40, 10, 20]
	Faça um programa que exclua todas as ocorrências do número 30 da lista

"""

lista = [10, 20, 30, 30, 30, 40, 10, 20]

while 30 in lista:
    lista.remove(30)

print("Lista sem as ocorrências do número 30:", lista)
