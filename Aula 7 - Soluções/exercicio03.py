# Exercício 03
# Escreva uma função com parâmetros que retorne o maior de dois
# números.
# ▶ A função deve se chamar maximo(x, y)

def maximo(x, y): # definindo a função
    if x > y: # verificando se x é maior que y
        return x # retornando x se for maior
    else:
        return y # retornando y se não for maior

# Exemplo de uso
resultado1 = maximo(10, 20) # chamando a função com os números 10 e 20
resultado2 = maximo(5, 15) # chamando a função com os números 5 e 15
print(f"O maior número entre 10 e 20 é: {resultado1}") # imprimindo o resultado
print(f"O maior número entre 5 e 15 é: {resultado2}") # imprimindo o resultado