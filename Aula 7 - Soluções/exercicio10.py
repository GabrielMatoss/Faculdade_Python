# Exercício 10
# Refaça os exercícios 3, 4, e 5 utilizando função lambda

## Exercício 3
maximo = lambda x, y: x if x > y else y # definindo a função lambda

# Exemplo de uso
resultado1 = maximo(10, 20) # chamando a função com os números 10 e 20
resultado2 = maximo(5, 15) # chamando a função com os números 5 e 15
print(f"O maior número entre 10 e 20 é: {resultado1}") # imprimindo o resultado
print(f"O maior número entre 5 e 15 é: {resultado2}") # imprimindo o resultado

## Exercício 4
multiplo = lambda x, y: True if x % y == 0 else False # definindo a função lambda
# Exemplo de uso
resultado1 = multiplo(10, 2) # chamando a função com os números 10 e 2
resultado2 = multiplo(10, 3) # chamando a função com os números 10 e 3
print(f"10 é múltiplo de 2? {resultado1}") # imprimindo o resultado
print(f"10 é múltiplo de 3? {resultado2}") # imprimindo o resultado

## Exercício 5
area_triangulo = lambda base, altura: (base * altura) / 2 # definindo a função lambda
# Exemplo de uso
resultado1 = area_triangulo(10, 5) # chamando a função com base 10 e altura 5
resultado2 = area_triangulo(8, 4) # chamando a função com base 8 e altura 4
print(f"A área do triângulo com base 10 e altura 5 é: {resultado1}") # imprimindo o resultado
print(f"A área do triângulo com base 8 e altura 4 é: {resultado2}") # imprimindo o resultado