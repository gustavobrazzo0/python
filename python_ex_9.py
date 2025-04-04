'''

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

'''

farenht = float(input("Informe a temperatura em farenheit: "))

celsius = 5 *((farenht - 32)/9)


print("A temperatura informada em farenheit são {} º Graus em celsius".format(celsius))