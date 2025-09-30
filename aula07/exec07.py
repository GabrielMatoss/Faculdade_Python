# Existem restrições para que uma pessoa possa doar sangue. Uma
# delas é relativa ao peso. Mulheres tem que pesar no mínimo
# 50kg e homens no mínimo 60kg. Faça uma função para informar
# se uma pessoa está ou não apta a doar sangue sabendo seu sexo
# e seu peso.
# O programa principal deve ler as entradas, acionar a função e
# exibir a resposta.

def pode_doar_sangue(sexo, peso):
    if (sexo == "F" and peso > 50) or (sexo == "M" and peso > 60):
        return True
    else:
        return False

sexoLocal = input("Informe F ou M: ")
pesoLocal = int(input("Informe o peso: "))
print("Pode doar? ", pode_doar_sangue(sexoLocal, pesoLocal))