# fazer o coeficiente binomial usando funções

n = int(input("digite um num int e positivo para ser o n: "))
p = int(input("digite um num int e positivo menor ou igual a n para ser o p: "))

def fatorial (x):
    fatorial1 = 1
    primeiro_num = 1
    while primeiro_num <= x:
        fatorial1 *= primeiro_num
        primeiro_num += 1
    return fatorial1

if n > 0 and p > 0 and n >= p:
    coef_binomial = fatorial(n) / (fatorial(p) * fatorial (n-p))
    print(coef_binomial)
else:
    print("n é possível coef binominal com n menor que p")           

# fatorial1 só sendo usado no escopo da função
# x teve q ser definido e colocado na função(x) pq iria ser usado no escopo
 
# resolução do professor:
 
def fatorial (n):
    fat = 1
    while (n > 1):
        fat *= n
        n -= n
    return fat

def numero_binomial (n, k):
    return fatorial (n) / (fatorial (k) * fatorial (n-k))

# aplicação de teste com funções:

def testa_fatorial ():
    if fatorial (1) == 1:
        print ("funciona para 1")
    else:
        print ("não funciona para 1")
    if fatorial (2) == 2:
        print ("funciona para 2")
    else:
        print ("não funciona para 2")
    if fatorial (0) == 1:
        print ("funciona para 0")
    else:
        print ("não funciona para 0")
    if fatorial (5) == 120:
        print ("funciona para 5")
    else:
        print ("não funciona para 5")            






    
    
    
    
    