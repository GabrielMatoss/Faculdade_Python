# Exercício 1
# Faça um programa que receba uma série de n;umeros naturaus e contabilize quantos desses números são primos. 
# Um número primo x é primo se x > 1 e seus únicos divisores são 1 e x.
 
numero = int(input("Digite a quantidade de números a serem testados: "))

primos = 0 # contador de números primos
for i in range(numero): # para cada número a ser testado
    n = int(input("Digite o número a ser testado: ")) # lê o número
    if n > 1: # se o número for maior que 1
        eh_primo = True # assume que o número é primo
        for j in range(2, n): # para cada número entre 2 e n
            if n % j == 0: # se n for divisível por j
                eh_primo = False  # n não é primo

        if eh_primo == True: # se n for primo
            primos = primos + 1 # incrementa o contador de primos
            print(f"O número {n} é primo") # imprime o número primo
        
print(f"a quantidade de números primos é {primos}") # imprime a quantidade de primos