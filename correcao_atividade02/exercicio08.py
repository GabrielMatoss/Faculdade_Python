# No exercício do PIM, a linha é um conjunto de valores derivados de um contador contínuo, então 
# você precisa de um loop interno para gerar essa coleção antes de finalizar a linha.

# Escreva um programa que leia um valor inteiro
# n, onde n
# é a quantidade de linhas de saída que serão apresentadas na execução do programa.
# A saída do programa deve ser feita seguindo o padrão dos exemplos fornecidos.

n = int(input("Digite um valor inteiro: "))
contador = 1

for linha in range(n):          # controla as linhas
    for i in range(3):          # controla os 3 números de cada linha
        print(contador, end=' ')
        contador += 1
    print("PIM")                # fecha a linha com 'PIM' só é exibido depois que o for acaba

# daria pra fazer sem for dentro do outro, porém nao ficaria muito legivel
# n = int(input("Digite um valor inteiro: "))
# contador = 1

#esse end no final serve para substituir o comportamento de quebra de linha do print()
# ai nesse caso só adicionamos os espaços
# for i in range(1, n * 3 + 1):
#     print(contador, end=' ')
#     if i % 3 == 0:  # a cada 3 números
#         print("PIM")
#     contador += 1
