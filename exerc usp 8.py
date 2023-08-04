# Escreva um programa que receba um número natural n na entrada e imprima n!
# n! (fatorial) na saída.
# Dica: lembre-se que o fatorial de 0 vale 1!
# corrigir: não existe fatorial de negativo

# como o chat gpt fez:
n = int(input("Digite o valor de n: "))

fatorial = 1
contador = 1

while contador <= n:
    fatorial *= contador
    contador += 1

print(fatorial)

# como eu fiz: 
n1 = int(input("digite o valor de n: "))

n = n1 + 1
antes_n = n - 1
if n == 1:
    antes_n = 1
n2 = n * antes_n
antes_n = antes_n - 1
while antes_n > 0:
    
    n2 = n2 * antes_n
    antes_n = antes_n - 1
   
n_fatorial = n2 / (n1+1)
   
print(int(n_fatorial))