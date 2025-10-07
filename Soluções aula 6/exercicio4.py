# Exercício 4
# Faça um programa que permita imprimir uma represetação de tabela quadrada com $ e @. 
# Nesta tabela o triangulo inferior esquerdo deve ser preenchido com $ e o triângulo superior direito deve ser preenchido com @.

linhas = int(input("Digite o tamanho da tabela: ")) # Informa o tamanho da tabela
for l in range(linhas): # Para cada linha
    for c in range(linhas): # Para cada coluna
        if c < l: # Se a coluna for menor que a linha
            print("$", end=" ") # Apresenta o caractere @
        else:
            print("@", end=" ") # Apresenta o caractere $
    print() # Ao fim de cada linha