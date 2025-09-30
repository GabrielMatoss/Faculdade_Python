# Use a função criada no exercício anterior
# Exiba todas as datas mágicas do século XX.
# Ou seja, do ano 1901 à 2000

def data_magica(d, m, a):
    if a % 100 == d * m:
        return True
    else:
        return False
    
for ano in range(1901, 2000):
    for mes in range(1, 12):
        for dia in range(1, 31):
            if data_magica(dia, mes, ano):
                print("eh mágica = ", dia, "/", mes, "/", ano)