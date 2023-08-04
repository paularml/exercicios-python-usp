# Receba um número inteiro positivo na entrada e imprima os n primeiros 
# números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int(input("digite o valor de n: "))
num = 0
while n > 0:
    num = num + 1
    par = num % 2
    if par != 0:
        print(num)
        n = n - 1 

