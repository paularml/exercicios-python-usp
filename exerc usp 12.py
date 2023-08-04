# reorganizar o exerc usp extra 3 (das raízes) usando funções
# talvez seja interessante colocar o cálculo de delta numa função tbm

import math
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
print() # pra pular linha

delta = float(b**2 - (4*a*c))

def raízes():
    if delta < 0:
        return print("esta equação não possui raízes reais")

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



import math
a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))
print()

#ajuda da poli cubos
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz, raiz
    else:
        return None