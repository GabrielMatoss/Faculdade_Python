#Faça um programa que peça ao usuário para digitar um número inteiro de 1 a 10 e 
#desenhe uma cruz usando o caractere + com base na entrada.
#O tamanho da cruz deve ser baseado em um número inteiro positivo fornecido pelo usuário, que determina o comprimento dos braços da cruz.
#Caso o número digitado não seja válido, o programa deve mostrar a mensagem (Número inválido)
#Listas Aninhadas
# Pede ao usuário para digitar um número inteiro.

numero = int(input("Digite o tamanho da cruz: "))
    # Verifica se o número está no intervalo válido de 1 a 10.
if 1 <= numero <= 10:
        # O tamanho total da grade será (numero * 2) - 1.
        # Ex: para 3, o tamanho é 5x5. Para 5, é 9x9.
    tamanho_total = (numero * 2) - 1
        # A posição do meio é o número digitado menos 1 (porque os índices começam em 0).
    meio = numero - 1
        # Laço 'for' aninhado para desenhar a cruz.
        # O primeiro laço (i) percorre as linhas.
    for i in range(tamanho_total):
            # O segundo laço (j) percorre as colunas de cada linha.
        for j in range(tamanho_total):
                # CONDIÇÃO 1: Verifica se a posição atual (i, j) é o centro exato da cruz.
            if i == meio and j == meio:
                    # Se for o centro, imprime o número digitado.
                print("+", end=" ")
                # CONDIÇÃO 2: Se não for o centro, verifica se está na linha ou coluna central.
            elif i == meio or j == meio:
                    # Se estiver, imprime o caractere '+'.
                print("+", end=" ")
                # CONDIÇÃO 3: Se não for nem o centro nem os braços da cruz.
            else:
                    # Imprime um espaço em branco.
                print(" ", end=" ")
            # Pula para a próxima linha ao final de cada linha da grade.
        print()

    # Se o número estiver fora do intervalo de 1 a 10.
else:
    print("Número inválido!")