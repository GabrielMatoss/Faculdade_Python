# Escreva um programa em Python que:

#     Peça ao usuário um número inteiro n entre 1 e 10.
#     Crie uma matriz n × n contendo apenas o número 0.
#     Exiba a matriz na tela se for possível.



# Solicita o número n
n = int(input("Digite o valor de n (entre 1 e 10): "))
#é basicamente um and se eu colocar and
if 1 <= n <= 10:
    resultado = "["
    for i in range(n):
        resultado += "["
        for j in range(n):
            resultado += "0"
            if j < n - 1:
                resultado += ", "
        resultado += "]"
        if i < n - 1:
            resultado += ", "
    resultado += "]"
    
    print(f"Matriz {n}x{n}: {resultado}")
else:
    print("Por favor, insira um número entre 1 e 10.")