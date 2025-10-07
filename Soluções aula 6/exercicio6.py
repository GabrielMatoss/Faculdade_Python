# Exercício 6
# Crie um progama que leia um número natural positivo N e determine quantos dígitos possui o número.
# Entrada: O programa recebe um número inteiro, N, maior que zero. 
# Saída: O programa deve imprimir a quantidade de dígitos do número N.

numero = int(input("Digite um número: ")) # Informa o número
digitos = 0 # Inicializa o contador de dígitos
while numero > 0: # Enquanto o número for maior que zero
    numero = numero // 10 # Divide o número por 10
    digitos = digitos + 1 # Incrementa o contador de dígitos
print(f"O número tem {digitos} dígitos") # Apresenta a quantidade