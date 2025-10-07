# Exercício 05
# Escreva uma função com parâmetros que:
# ▶ Receba a base e a altura de um triângulo e retorne sua área

def area_triangulo(base, altura): # definindo a função
    area = (base * altura) / 2 # calculando a área do triângulo
    return area # retornando a área

# Exemplo de uso
resultado1 = area_triangulo(10, 5) # chamando a função com base 10 e altura 5
resultado2 = area_triangulo(8, 4) # chamando a função com base 8 e altura 4
print(f"A área do triângulo com base 10 e altura 5 é: {resultado1}") # imprimindo o resultado
print(f"A área do triângulo com base 8 e altura 4 é: {resultado2}") # imprimindo o resultado