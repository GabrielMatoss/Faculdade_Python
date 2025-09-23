# Escreva uma função com parâmetros chamada multiplo(x, y).
# ▶ Esta função deve receber dois números
# ▶ Retornar True se o primeiro for múltiplo do segundo número;
# ▶ Retornar False caso contrário.

def multiplo(x, y):
    res = x % y == 0
    if(res):
        return res
    return res


value = int(input("Digite um valor: "))
value2 = int(input("Digite o segundo valor: "))
print(multiplo(value, value2))
