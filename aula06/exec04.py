maior = 0
for i in range(7):
    num = int((input("Digite um valor inteiro e positivo:")))
    if num > maior:
        maior = num
print(f"O maior número digitado foi: {maior}")

# # --- Utilizando laço de repetição while ---
# count = 0 # inicializa o contador
# maior = 0 # inicializa a variável maior
# while count < 6: # Enquanto o contador for menor que 6
#     num = int(input("Digite um número inteiro positivo: ")) # Solicita ao usuário um número
#     if num > maior: # Se o número digitado for maior que o maior
#         maior = num # Atualiza o maior
#     count = count + 1 # Incrementa o contador 
