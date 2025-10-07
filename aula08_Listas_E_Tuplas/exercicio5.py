lista = []
qtd = int(input("Digite  a quantidade de números: "))

for i in range(qtd):
    nro = int(input("Digite um número: "))
    lista.append(nro)

print("Números: ", lista)
print("Inverso: ")

for i in range(len(lista) -1, -1, -1):
    print(lista[i])