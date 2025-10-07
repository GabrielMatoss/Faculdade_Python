lista = []

for i in range(10):
    nro = int(input("Digite um número: " ))
    lista.append(nro)

print(lista)

for i in range(2, 10):
    if lista[i] > (lista[i - 1] + lista[i - 2]):
        print(lista(i))
        