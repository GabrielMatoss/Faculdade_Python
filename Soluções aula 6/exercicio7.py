# Exercício 7
# Crie um porgama que permita verificar se um número pertence a sequência de Fibonacci.
# A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores.
# Entrada: O programa recebe um número inteiro, N, maior que zero.
# Saída: O programa deve imprimir "verdadeiro" se o número N pertence ou "Falso" caso não pertença à sequência de Fibonacci.

numero = int(input("Digite um número: ")) # Informa o número
a = 0 # Initializa o primeiro número da sequência de Fibonacci
b = 1 # Inicializa o segundo número da sequência de Fibonacci 

while a <= numero: # Enquanto o primeiro número for menor ou igual ao número informado
    if a == numero: # Se o número informado for igual ao primeiro número
        print("Verdadeiro") # Apresenta Verdadeiro
        break # Interrompe o laço
    c = a + b # Calcula o próximo número da sequência
    a = b # Atualiza o primeiro número
    b = c # Atualiza o segundo número
    # As 3 linhas acima podem ser substituídas por: a, b = b, a + b 

if a > numero: # Se o primeiro número for maior que o número informado
    print("Falso") # Apresenta Falso

    
