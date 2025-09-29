# Faça um programa que leia do usuário um número inteiro de 1 a 10 e exiba todos os pares de números inteiros 
# (i, j) onde i e j variam de 1 até o número digitado.
# Para cada par (i, j), o programa deve exibir a soma de i + j.
# Caso o número digitado não seja válido, o programa deve mostrar a mensagem (Número inválido!).
# Solicita ao usuário um número e o converte para o tipo inteiro.

numero = int(input("Digite um número de 1 a 10: "))

    # Verifica se o número está no intervalo válido de 1 a 10.
if numero >= 1 and numero < 10: #nesse caso tive que fazer assim pq o exercício pedia
        # Loop externo para a variável 'i', que vai de 1 até o número digitado.
    for i in range(1, numero + 1):
            # Loop interno para a variável 'j', que também vai de 1 até o número digitado.
        for j in range(1, numero + 1):
                # Calcula a soma de i e j.
            soma = i + j
                # Exibe o par (i, j) e sua respectiva soma no formato solicitado.
            print(f"Par ({i}, {j}) - Soma: {soma}")
else:
        # Se o número estiver fora do intervalo, exibe a mensagem de erro.
    print("Número inválido!")