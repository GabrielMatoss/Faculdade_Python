# Exercício 07
# Existem restrições para que uma pessoa possa doar sangue. Uma
# delas é relativa ao peso. Mulheres tem que pesar no mínimo
# 50kg e homens no mínimo 60kg. Faça uma função para informar
# se uma pessoa está ou não apta a doar sangue sabendo seu sexo
# e seu peso.
# O programa principal deve ler as entradas, acionar a função e
# exibir a resposta.

def doar_sangue(sexo, peso): # definindo a função
    if (sexo == 'F' and peso >= 50) or (sexo == 'M' and peso >= 60): # verificando as condições para doação
        return True # retornando True se a pessoa está apta a doar
    else:
        return False # retornando False se a pessoa não está apta a doar

# Exemplo de uso
sexo = input("Informe o sexo (F/M): ") # lendo o sexo da pessoa
peso = float(input("Informe o peso: ")) # lendo o peso da pessoa
resultado = doar_sangue(sexo, peso) # chamando a função com os dados informados
if resultado: # verificando o resultado
    print("A pessoa está apta a doar sangue.") # imprimindo se a pessoa está apta
else:
    print("A pessoa não está apta a doar sangue.") # imprimindo se a pessoa não está apta