"""3. Leia um número e imprima a tabuada de multiplicar deste número."""

numero = int(input("Digite um número: "))
for i in range(1,11):
  print(numero, "x", i, "=",numero*i)
