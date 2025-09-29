# Escreva uma função que tenha os comprimentos dos dois lados mais curtos de um triângulo retângulo
# como seus parâmetros. Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras, 
# como o resultado da função. Inclua um programa principal que lê os comprimentos dos lados mais curtos 
# de um triângulo retângulo do usuário e use sua função para calcular o comprimento da hipotenusa. 
# Exiba o resultado.

#Calcular a hip usando Pitagoras (sem usar a biblioteca math é elevar a 0.5)
import math

def calc_triangulo(b, c):
    x = math.sqrt(b**2 + c**2)
    return x

def ler_entredas():
    primeiro_lado = int(input("Digite o primeiro lado do triângulo: "))
    segundo_lado = int(input("Digite o segundo lado do triângulo: "))

    hipotenusa = calc_triangulo(primeiro_lado, segundo_lado)
    print(f"Hipotenusa: {hipotenusa:.2f}")

ler_entredas()
    