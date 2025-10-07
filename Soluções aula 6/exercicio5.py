# Exercício 5
# Faça um programa que permita imprimir uma representação da tabela quadrada seguindo o padrão. 

tamanho = int(input("Digite o tamanho da tabela: ")) # Informa o tamanho da tabela
for l in range(tamanho): # Para cada linha
    for c in range(tamanho): # Para cada coluna
        if l % 2 == 0: # Se a linha for par
            if c % 2 == 0: # Se a coluna for par
                print("$", end=" ")
            else: # Se a coluna for ímpar
                print("&", end=" ")
        else: # Se a linha for ímpar
            if c % 2 == 0: # Se a coluna for par
                print("%", end=" ")
            else:
                print("#", end=" ")
            
    print() # Ao fim de cada linha pula para a próxima linha