from random import randint, random
# print(randint(0, 10))#inteiros
# print(random() * 10)#reais

lista_int = []
lista_float = []
lista_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lista_geral = []

for i in range(10):
    nro = randint(0, 10)
    lista_int.append(nro)

for i in range(5):
    nro = random() * 10
    lista_float.append(nro)

lista_geral.append(lista_int)
lista_geral.append(lista_float)
lista_geral.append(lista_string)

#apagamos as listas para mostrar que nao importa quando colocamos tudo numa lista maior
del(lista_int)
del(lista_float)
del(lista_string)

print(lista_geral)