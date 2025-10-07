# Uma loja dá desconto de 10% para compras à vista, 5% para compras em 2 ou 3 parcelas e não dá desconto para 
# compras acima de 3 parcelas. Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao 
# outro possível desconto) aos clientes que comprarem um total superior a R$5.000,00. 
# Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor do desconto,  
# o valor final da compra com desconto e o valor de cada parcela.
# Utilize duas casas decimais.


# Leitura dos dados
valor_compra = float(input("Digite o valor total da compra: R$ "))
parcelas = int(input("Digite o número de parcelas: "))

# Definição do desconto base
if parcelas == 1:
    desconto = 0.10  # 10% à vista
elif parcelas == 2 or parcelas == 3:
    desconto = 0.05  # 5% para 2 ou 3 parcelas
else:
    desconto = 0.0   # Sem desconto acima de 3 parcelas

# Desconto adicional se valor > 5000
if valor_compra > 5000:
    desconto += 0.05  # Soma mais 5%


# Em Python, se você cria uma variável fora de uma função, ela tem escopo global 
# dentro do bloco atual (por exemplo, dentro do mesmo script ou função).
# nesse caso a variavel desconto é global por estar fora de uma função.
# Por isso ela pode ser modificada posteriormente!
# Cálculos finais
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto
valor_parcela = valor_final / parcelas

# Exibição formatada
print(f"\nDesconto total: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")