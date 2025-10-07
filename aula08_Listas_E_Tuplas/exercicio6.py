temp = [-10, -8, 0, 1, 2, 5, -2, -4]

soma_temp = 0
menor_temp = 999
maior_temp = -999

for i in range(len(temp)):
    soma_temp += temp[i]
    if temp[i] > maior_temp:
        maior_temp = temp[i]
    if temp[i] < menor_temp:
        menor_temp = temp[i]

print("Maior: ", maior_temp)
print("Menor: ", menor_temp)
print("Media: ", soma_temp/len(temp))
