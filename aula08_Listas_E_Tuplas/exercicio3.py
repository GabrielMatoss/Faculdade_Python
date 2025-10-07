# Faça um programa para criar uma lista de 10 elementos do
# usuário e aprsente:
# ▶ a soma dos elementos pares
# ▶ a soma dos elementos de índice par

lista = []
soma_elementos_par = 0
soma_idx_par = 0

for idx in range(10):
    nro = int(input("Digite um número: "))
    lista.append(nro)
    if idx % 2 == 0:
        soma_idx_par += soma_idx_par + nro

    if nro % 2 == 0:
        soma_elementos_par += nro
#soma dos elementos indices pares
print(lista)
print("Soma dos elementos de idx pares = ", soma_idx_par) 
print("Soma dos elementos pares = ", soma_elementos_par) 