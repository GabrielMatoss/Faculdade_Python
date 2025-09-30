# Funções
# Exercício 08
# Uma data é considerada mágica quando o dia multiplicado pelo
# mês é igual ao ano de dois dígitos.
# Por exemplo, 10 de junho de 1960 é uma data mágica porque
# junho é o sexto mês e 6 vezes 10 é 60, o que equivale ao ano
# de dois dígitos. 
# (o resto de 1960 % 100 é 60 pois para na parte inteira)
# Escreva uma função que determine se uma data é ou não uma data
# mágica

def data_magica(d, m, a):
    if a % 100 == d * m:
        return True
    else:
        return False
    
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))
print("É uma data mágica? ", data_magica(dia, mes, ano))