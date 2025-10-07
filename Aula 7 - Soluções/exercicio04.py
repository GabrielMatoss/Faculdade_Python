# Exercício 04
# Escreva uma função com parâmetros chamada multiplo(x, y).
# ▶ Esta função deve receber dois números
# ▶ Retornar True se o primeiro for múltiplo do segundo número;
# ▶ Retornar False caso contrário.

def multiplo(x, y):
    if x % y == 0: # verificando se x é múltiplo de y
        return True # retornando True se for múltiplo
    else:
        return False # retornando False se não for múltiplo

# Exemplo de uso
resultado1 = multiplo(10, 2) # chamando a função com os números 10 e 2
resultado2 = multiplo(10, 3) # chamando a função com os números 10 e 3
print(f"10 é múltiplo de 2? {resultado1}") # imprimindo o resultado
print(f"10 é múltiplo de 3? {resultado2}") # imprimindo o resultado