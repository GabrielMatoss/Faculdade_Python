# Exercício 1
# Crie uma função que calcule a média de dois números
#  ▶ Sua função deve receber dois números como parâmetros de entrada
#  ▶ Deve imprimir o resultado da média

def media(num1, num2): # definindo a função
    resultado = (num1 + num2) / 2 # calculando a média
    print(f"A média de {num1} e {num2} é: {resultado}") # imprimindo o resultado
    
# Exemplo de uso
media(10, 20) # chamando a função com os números 10 e 20
media(5, 15) # chamando a função com os números 5 e 15