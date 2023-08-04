#um programa que confira a raíz da equação quadrática

a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
print()

import math
delta = float(b**2 - (4*a*c))
if delta < 0:
    print("A equação não possui qualquer raiz real. Em vez disso, ela possui duas raízes complexas distintas, que são conjugadas uma da outra.")
else:
    x1 = (-(b) + (math.sqrt(delta))) / 2*a
    x2 = (-(b) - (math.sqrt(delta))) / 2*a
if delta == 0:
    x1= -(b)/(2*a)         
    print("Essa equação só tem uma raiz: ", x1)

if delta > 0:
    print ("A equação tem duas raízes reais e distintas: ", x1, "e", x2)

print()

