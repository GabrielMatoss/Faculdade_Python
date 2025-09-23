# Faça um programa que:
# ▶ Leia três números e apresente o resultado do seguinte cálculo:

# def calcula(x, y, z):
#    raiz1 =  x ** 0.5
#    raiz2 = y ** 0.5
#    raiz3 = z ** 0.5
#    resultado = (raiz1 + raiz2 + raiz3) + (x + y) / 2 + (y + z) / 2 + (x + z) / 2
#    return resultado

# value = int(input("Digite um valor: "))
# value2 = int(input("Digite o segundo valor: "))
# value3 = int(input("Digite o terceiro valor: "))
# print(calcula(value, value2, value3))

##Versao da professora
#Ela pegou trechos que se repetiam e encapsulou em funções
#auxiliar
def raiz(z):
    return z**0,5

def media(x, y):
    return (x + y) / 2

#principal
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

resultado = raiz(n1) + raiz(n2) + raiz(n3) + media(n1, n2) + media(n2, n3) + media(n1, n3)