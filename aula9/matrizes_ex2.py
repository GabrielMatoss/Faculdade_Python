#Criar uma Matriz M, 10 x 15, cujos elementos são iguais a somatória de sua linha com sua coluna(elemeto = linha + coluna)
M = []

for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
    M.append(linha)

#Exibindo os elementos da matriz M:
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%4d" % M[linha][coluna], end= "")
    print()

    #%4d faz ocupar 4 posições, mesmo que tenha só um caracter, exemplo 10 fica com 2 espaços em branco, assim fica mais alinhado