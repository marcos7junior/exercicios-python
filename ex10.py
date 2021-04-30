"""
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
F=1,8C+32
"""

temp_celsius = float(input("Digite o valor da temperatura em graus Celsius: "))

temp_fahr = 1.8*temp_celsius + 32

print("{:.1f}°C vale {:.1f}°F".format(temp_celsius, temp_fahr))

