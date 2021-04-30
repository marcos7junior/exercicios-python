"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input("Valor da hora trabalhada: "))
horas_mes = int(input("Quantos horas trabalha por mes? "))

salario = valor_hora*horas_mes

print("O salario é R$6{}".format(salario))
