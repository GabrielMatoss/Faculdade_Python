# Exercício 08
# Uma data é considerada mágica quando o dia multiplicado pelo
# mês é igual ao ano de dois dígitos.
# Por exemplo, 10 de junho de 1960 é uma data mágica porque
# junho é o sexto mês e 6 vezes 10 é 60, o que equivale ao ano
# de dois dígitos.
# Escreva uma função que determine se uma data é ou não uma data
# mágica.
# Exemplo

def data_magica(dia, mes, ano): # definindo a função
    ano_dois_digitos = ano % 100 # obtendo os últimos dois dígitos do ano
    if dia * mes == ano_dois_digitos: # verificando se a data é mágica
        return True # retornando True se for mágica
    else:
        return False # retornando False se não for mágica
    
# Exemplo de uso

resultado = data_magica(6, 10, 1960) # chamando a função com os dados informados
print(f"A data 6/10/1960 é mágica? {resultado}") # imprimindo o resultado
resultado = data_magica(5, 5, 2005) # chamando a função com os dados informados
print(f"A data 5/5/2005 é mágica? {resultado}") # imprimindo o resultado
