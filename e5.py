print("Escreva um programa que converta uma temperatura de graus Celsius para graus Fahrenheit")

cel = float(input('\nDigite a temperatura em °C: '))

#Formula para conversão de Celsius para Fahrenheit: C° * 1.800 + 32
print('\nA temperatura em graus Fahrenheit é: {} °F' .format(cel * 1.800 + 32))

#Formula para conversão de Celsius para Kelvin: C° + 273.15
print('A temperatura em graus Kelvin é: {} °K' .format(cel + 273.15))