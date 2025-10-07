# Exercício 13
# Escreva uma função chamada exponencial que recebe um valor n
# como parâmetro. Sua função deve encontrar e retornar b e k tal
# que b^k = n e b seja o menor possível.

def exponencial(n): # definindo a função
    if n == 1:
        print("1 é uma potência de qualquer número. Logo b = 1 e k = 0")
    
    b = 2 # inicializando b com 2
    while True: # loop infinito
        k = 0 # inicializando k
        resultado = 1 # inicializando resultado com 1
        while resultado < n: # enquanto o resultado for menor que n
            resultado = resultado * b # multiplicando o resultado por b
            k = k + 1 # incrementando k
            
        if resultado == n: # verificando se o resultado é igual a n
            print(f"{n} = {b}^{k}")
            break
        else:
            b = b + 1 # incrementando b para tentar o próximo número