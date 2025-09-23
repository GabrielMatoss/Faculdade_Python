# Crie uma função que calcule a média de dois números
# ▶ Sua função deve receber dois números como parâmetros de entrada
# ▶ Deve imprimir o resultado da média


#auxiliar
def media(x, y):
    res = (x + y) / 2
    return  res
#principal
value = int(input("Digite um valor: "))
value2 = int(input("Digite o segundo valor: "))

print("A média aritmética é: ", media(value, value2));