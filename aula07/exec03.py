# Escreva uma função com parâmetros que retorne o maior de dois
# números.
# ▶ A função deve se chamar maximo(x, y)

def retorna_maior(x, y):
    if(x > y):
        return  x;
    elif(x < y):
        return y;
    else:
        return "Ambos valores são iguais!"


value = int(input("Digite um valor: "))
value2 = int(input("Digite o segundo valor: "))

print(retorna_maior(value, value2))