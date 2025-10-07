# Escreva um programa que leia um valor inteiro n, onde n
# é a quantidade de linhas de saída que serão apresentadas na execução do programa.
# A saída do programa deve ser feita seguindo o padrão dos exemplos fornecidos.

n = int(input("Digite um valor inteiro: "))

for i in range(1, n + 1):
    print(i, i**2, i**3)
#No exercício das potências, a linha é auto-contida: um único i gera todos os valores.
#por isso nao é necessário um for dentro do outro