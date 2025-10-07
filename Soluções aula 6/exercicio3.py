# Exercício 3
# Faça um program que permita imprimir uma representação de um tabuleiro de xadrez utilizando os caracteres "o" e "x".
# O canto superior esquerdo do tabuleiro deve ser preenchido com o caractere "o".

linhas = int(input("Digite o tamanho do tabuleiro: ")) # Informa o tamanho do tabuleiro

for l in range(linhas): # Para cada linha
    for c in range(linhas): # Para cada coluna
        if (l + c) % 2 == 0: # Se a soma da linha e coluna for par
            print("o", end=" ") # Apresenta o caractere o
        else:
            print("x", end=" ") # Apresenta o caractere x
    print() # Ao fim de cada linha, pula para a próxima linha