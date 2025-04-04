'''

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

'''

altura = float(input("informe sua altura para saber seu peso ideal: "))

peso_ideal = (72.7 * altura) - 58

print("De acordo com sua altura, seu peso ideal é {}".format(peso_ideal))