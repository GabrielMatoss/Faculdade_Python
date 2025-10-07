z = ['a', 'b', 'c', 'd', 'e']

#note que usamos o for in e não o for com o range pois estamos iterando sobre uma lista
for elemento in z:
    if elemento == 'c':
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado!")

#podemos fazer mais simples, pois só estamos avisando se o elemento está na lista ou não
if 'c' in z:
    print("Encontrado")
else:
    print("Não encontrado!")

#se precisamos falar o indice temos que usar o range mesmo
for indice in range(len(z)):
    if z[indice] == 'c':
        print("Elemento encontrado no indice %d" % indice)
        break #quebra o laço e segue com o código
else:
    print("Elemento não encontrado!")