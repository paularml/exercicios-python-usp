# um programa q diga se um num tem dois dígitos adjacentes iguais usando 
# indicador de passagem

num = int(input("Digite um número inteiro: "))

adjacente = False
        
while num != 0 and not adjacente:
    digito_prox = num % 10
    num = num // 10
    digito = num % 10
    if digito == digito_prox:
        adjacente = True
        if adjacente == True:
            print("sim")

if adjacente == False:
    print("não")        
   #while: esse comando é utilizado qnd n se sabe o num de vezes que
   # um algoritmo deve ser repetido. Esse comando possui uma condição
   # (ou expressão lógica) inicial, ou seja, só permite a execução
   # de um ou mais comandos se a condição for verdadeira.
   # por isso o uso do NOT, para a condição se tornar verdadeira e o 
   # while poder rodar. qnd a expressão se tornou verdadeira de vdd
   # então o NOT faria ela se tornar falsa e então o while pararia
   # e num != 0 é uma expressão verdadeira, qnd chega a 0 se torna falsa
   # looping pré testado (tem q ser verdadeiro para rodar o while)# 
   #prestar MUITA atenção no quanto uma condição deve se repetir ou não