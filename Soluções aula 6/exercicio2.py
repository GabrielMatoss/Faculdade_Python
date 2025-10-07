# Exercício 2
# Faça um porgrama que permita imprimir apenas as bordas de um retângulo. 
# O programa deve receber dois números inteiros L > 0 e C > 0, que representam a quantidade de linhas e colunas do retângulo, respectivamente.

linhas = int(input("Digite a quantidade de linhas: ")) # Informa a quantidade de linhas
colunas = int(input("Digite a quantidade de colunas: ")) # Informa a quantidade de colunas

for l in range(linhas): # Para cada linha
    for c in range(colunas): # Para cada coluna
        if l == 0 or l == linhas - 1 or c == 0 or c == colunas - 1: # Se for a primeira ou última linha ou coluna
            print("*", end=" ") # Apresenta o caractere * e mantém o cursor na mesma linha
        else: 
            print(" ", end=" ") # Apresenta um espaço e mantém o cursor na mesma linha
    print() # Ao fim de cada linha, pula para a próxima linha
    
    