# Escreva um programa que receba um número inteiro positivo na entrada e 
# verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, 
# imprima "não primo".

num = int(input("digite um num: "))

primo = True
if num % 3 == 0 and num != 3 or num % 2 == 0 and num != 2 or num % 5 == 0 and num != 5 or num % 7 == 0 and num != 7:
    primo = False
    if primo == False:
        print("não primo")
else:
    print("primo")    
