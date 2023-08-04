#programa que recebe núm e diz as raízes da equação em ordem crescente
import math
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
print() # pra pular linha


delta = float(b**2 - (4*a*c))
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    x1 = (-(b) + (math.sqrt(delta))) / 2*a
    x2 = (-(b) - (math.sqrt(delta))) / 2*a
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
if delta == 0:
    x1= -(b)/(2*a)         
    print("a raiz desta equação é", x1)
