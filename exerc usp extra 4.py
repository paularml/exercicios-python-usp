# número grande e um programa pra calcular a soma dos dígitos desse número
num = int(input("Digite um número grande: "))


soma = 0 
while num > 0:
    digitos = num % 10        
    num = num // 10
    soma += digitos         

print ("A soma dos dígitos é: ", soma)

#aprendi a dividir o problema por partes
#em while é melhor começar pela solução do problema do que do começo
#pensar nos seus parâmetros primeiro, os de repetição e parada
#parametro de entrada do problema (soma=0), o num se tornou um parametro
#que teria que chegar a zero para o laço para, dps digitos, num mudando
#pro digito tb mudar e por fim soma somando os digitos até o num chegar a zero
#ou seja tds os numeros de 1234 eliminados