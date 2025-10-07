# Exercício 06
# Faça um programa que:
# ▶ Leia três números e apresente o resultado do seguinte cálculo:
# √n1 +√n2 +√n3 + (n1 +n2)/2+ (n2 +n3)/2 + (n1 +n3)/2
# Import a função sqrt do módulo math se necessário.

def calculo(n1, n2, n3): # definindo a função
    resultado = (n1**0.5 + n2**0.5 + n3**0.5) + ((n1 + n2) / 2) + ((n2 + n3) / 2) + ((n1 + n3) / 2) # realizando o cálculo
    return resultado # retornando o resultado

# Exemplo de uso
resultado1 = calculo(4, 9, 16) # chamando a função com os números 4, 9 e 16
resultado2 = calculo(1, 4, 9) # chamando a função com os números 1, 4 e 9
print(f"O resultado do cálculo com 4, 9 e 16 é: {resultado1}") # imprimindo o resultado
print(f"O resultado do cálculo com 1, 4 e 9 é: {resultado2}") # imprimindo o resultado