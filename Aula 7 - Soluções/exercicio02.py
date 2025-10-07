# Exercício 2
# Adapte a função para calcular a média criada anteriormente.
#  ▶ Faça com que ela retorne o resultado da média para o chamador da
#  função.

def media(num1, num2): # definindo a função
    resultado = (num1 + num2) / 2 # calculando a média
    return resultado # retornando o resultado
# Exemplo de uso
resultado1 = media(10, 20) # chamando a função com os números 10 e 20
resultado2 = media(5, 15) # chamando a função com os números 5 e 15
print(f"A média de 10 e 20 é: {resultado1}") # imprimindo o resultado
print(f"A média de 5 e 15 é: {resultado2}") # imprimindo o resultado