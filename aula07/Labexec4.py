# Escreva uma função com parâmetros que retorne o maior de dois números. 
# A função deve se chamar maximo(x, y), esse função também deverá ter mais 
# um parâmetro opcional chamado imprime, que por padrão é Falso, mas quando True,
# deverá imprimir o valor máximo.


def maximo(x, y, imprime = False):
    if(x > y and imprime != False):
        print(x)
    elif(x < y and imprime != False):
        print(y)

    if x > y:
        return x
    elif x < y:
        return y
        
    
print(maximo(1, 2))
maximo(1, 2, True)

#código mais simples
# def maximo(x, y, imprime=False):
#     if x > y:
#         maior = x
#     else:
#         maior = y
    
#     if imprime:
#         print(maior)
    
#     return maior


# # Exemplos de uso:
# print(maximo(1, 2))      # imprime 2 no terminal (porque o print externo mostra o retorno)
# maximo(7, 20, True)      # imprime 20 dentro da função
