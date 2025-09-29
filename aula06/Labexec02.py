# Faça um programa que leia do usuário um número inteiro de 1 a 10 e 
# calcule o fatorial de todos os números de 1 até o número digitado. 
# O fatorial de um número é o produto de todos os inteiros positivos de 1 até esse número. 
# O programa deve exibir o fatorial de cada número individualmente.
# Caso o número digitado não seja válido, o programa deve mostrar a mensagem (Número inválido!).

# num = int(input("Digite um número de 1 a 10: "))
# result = 1

# if num >= 1 and num <= 10:
#     for i in range(1, num + 1):
#         result *= i
#     print(f"Fatorial de {num} = {result}")
# else:
#     print("Número inválido!")



    # 1. Lê o número do usuário e converte para inteiro
numero_limite = int(input("Digite um número de 1 a 10: "))

    # 2. Verifica se o número está no intervalo válido (entre 1 e 10)
if numero_limite >=1 and numero_limite <= 10:
        # 3. Loop EXTERNO: Itera de 1 até o número que o usuário digitou.
        #    A variável 'i' representará cada número do qual queremos o fatorial (1, 2, 3, ...)
    for i in range(1, numero_limite + 1):    
            # 4. Inicializa o fatorial como 1 ANTES de começar o cálculo para um novo número 'i'
        fatorial_resultado = 1
            # 5. Loop INTERNO: Calcula o fatorial do número 'i' atual.
            #    A variável 'j' vai de 1 até 'i', fazendo as multiplicações.
        for j in range(1, i + 1):
            fatorial_resultado = fatorial_resultado * j
            # 6. Mostra o resultado para o número 'i' atual antes de ir para o próximo
        print(f"Fatorial de {i} = {fatorial_resultado}")
            
else:
    # 7. Mensagem para números fora do intervalo
    print("Número inválido!")