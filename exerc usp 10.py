# Escreva um programa que receba um número inteiro na entrada, calcule 
# e imprima a soma dos dígitos deste número na saída

num1 = int(input("digite um nume inteiro: "))
num_final = 0
while num1 > 0:
    num = num1 % 10
    num_final =+ num_final + num
    num1 = num1 // 10
print (num_final)    

