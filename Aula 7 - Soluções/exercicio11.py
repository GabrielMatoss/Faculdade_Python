# Exercício 11
# Faça uma função que receba quatro valores: I, A, B e C.
# Destes valores, I é um valor inteiro valendo 1, 2 ou 3. A, B
# e C são valores reais. Escreva os números A, B e C obedecendo
# à tabela a seguir, dependendo do valor de I

# - Valor de I = 1 -> A, B e C em ordem crescente
# - Valor de I = 2 -> A, B e C em ordem decrescente
# - Valor de I = 3 -> O maior fica entre os outros dois números

def maior_numero(A, B, C): # definindo a função
    if A >= B and A >= C: # verificando se A é o maior
        return A # retornando A se for o maior
    elif B >= A and B >= C: # verificando se B é o maior
        return B # retornando B se for o maior
    else:
        return C # retornando C se não for A nem B
    
def menor_numero(A, B, C): # definindo a função
    if A <= B and A <= C: # verificando se A é o menor
        return A # retornando A se for o menor
    elif B <= A and B <= C: # verificando se B é o menor
        return B # retornando B se for o menor
    else:
        return C # retornando C se não for A nem B

def meio_numero(A, B, C): # definindo a função
    if (A >= B and A <= C) or (A <= B and A >= C): # verificando se A está entre B e C
        return A # retornando A se estiver entre B e C
    elif (B >= A and B <= C) or (B <= A and B >= C): # verificando se B está entre A e C
        return B # retornando B se estiver entre A e C
    else:
        return C # retornando C se não for A nem B

def ordenar_numeros(I, A, B, C): # definindo a função
    maior = maior_numero(A, B, C) # chamando a função para obter o maior número
    menor = menor_numero(A, B, C) # chamando a função para obter o menor número
    meio = meio_numero(A, B, C) # chamando a função para obter o número do meio
    
    if I == 1:
        print(f"Números em ordem crescente: {menor}, {meio}, {maior}")
    elif I == 2:
        print(f"Números em ordem decrescente: {maior}, {meio}, {menor}")
    elif I == 3:
        print(f"O maior no meio: {menor}, {maior}, {meio}")
    else:
        print("Valor de I inválido. Deve ser 1, 2 ou 3.")
        
# Exemplo de uso
ordenar_numeros(1, 10, 5, 8) # chamando a função com I = 1
ordenar_numeros(2, 10, 5, 8) # chamando a função com I = 2
ordenar_numeros(3, 10, 5, 8) # chamando a função com I = 3
