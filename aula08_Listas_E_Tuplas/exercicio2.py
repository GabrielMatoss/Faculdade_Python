# Peça 10 números reais do usuário.
# ▶ Armazene-os em uma lista e diga qual o índice do maior e seu
# valor

# for i in range(11):
#     n = int(input("Digite um valor: "))
#     numeros = [] 
#     numeros.append(n)
# #menor valor por isso é engativo
# menor = -9999
# for indice in range(len(numeros)):
#     if numeros[indice] < menor:
#      menor = numeros[indice]
# print(numeros)

#poderia ter salvado o maior indice, seria mais facil
#soolução da prof

lista = []
maior = -9999 #quero mudar essa estratégia
idx_maior = -1

for idx in range(10):
    nro = int(input("Digite um número: "))
    lista.append(nro)
    if lista[idx] > maior:
        maior = lista[idx]
        idx_maior = idx

print(lista)
print("Maior = ", maior)
print("Indice do maior = ", idx_maior)
