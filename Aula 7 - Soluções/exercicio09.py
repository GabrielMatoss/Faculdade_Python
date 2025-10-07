# Exercício 09
# Use a função criada no exercício anterior
# Exiba todas as datas mágicas do século XX.
# Ou seja, do ano 1901 à 2000

def data_magica(dia, mes, ano): # definindo a função
    ano_dois_digitos = ano % 100 # obtendo os últimos dois dígitos do ano
    if dia * mes == ano_dois_digitos: # verificando se a data é mágica
        return True # retornando True se for mágica
    else:
        return False # retornando False se não for mágica
    
def datas_magicas(ano_inicio, ano_fim): # definindo a função para exibir as datas mágicas
    for ano in range(ano_inicio, ano_fim + 1): # iterando pelos anos
        for mes in range(1, 13): # iterando pelos meses de 1 a 12
            for dia in range(1, 32): # iterando pelos dias de 1 a 31
                if data_magica(dia, mes, ano): # verificando se a data é mágica
                    print(f"A data {dia}/{mes}/{ano} é mágica.") # imprimindo a data mágica
                    
# Exemplo de uso
datas_magicas(1901, 2000) # chamando a função para exibir as datas mágicas do século XX