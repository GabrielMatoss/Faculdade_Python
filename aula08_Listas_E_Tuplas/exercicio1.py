# Mostre o menor valor dentro da lista T = [11, 7, 2, 4]
T = [11, 7, 2, 20]
menor = 9999 #estrategia de estouro do contador, inicializando com um valor absurdo
for indice in range(len(T)):
    if T[indice] < menor:
        menor = T[indice]

print(menor)
     
#se tivessemos que receber os valores via teclado teria que ter um for para pegar os valores e depois iterar os valores onde pegamos
