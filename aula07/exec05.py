# Escreva uma função com parâmetros que:
# ▶ Receba a base e a altura de um triângulo e retorne sua área
#Área = (base × altura) / 2

def area_triangulo(x, y):
    res = (x * y) / 2
    return res
    #poderiamos colocar o calculo direto no return
    #nao precisaria dos parenteses, pq a ordem seria da esquerda para a direita

value = int(input("Digite um valor: "))
value2 = int(input("Digite o segundo valor: "))

print("A aréa do triangulo é de: ", area_triangulo(value, value2))