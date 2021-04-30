"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

altura = float(input("Qual a sua altura? "))
sexo = input("Digite m para masculino e f para feminino: ")

if sexo == "m":
    peso_ideal = (72.7*altura) - 58
    print(peso_ideal/100)
elif sexo == "f":
    peso_ideal = (62.1*altura) - 44.7
    print(peso_ideal/100)
else:
    print("Valor invalido")
