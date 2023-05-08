import math

#Solicita os coeficientes a,b e c da equação do segundo grau
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

#Calcula o discriminante da equação 
delta = b**2 - 4*a*c

#Calcula as raízes da equação
if delta < 0:
    print("A equação não possui raízes reais.")

elif delta == 0:
    x = -b / (2*a)
    print("A equação possui uma raiz real:", x)

else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("A equação possui duas raízes reais", x1, "e", x2)