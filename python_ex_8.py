'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''

## horacifrao = valor ganho por hora
## htrabalhadas = horas trabalhadas
## salmes = salário do mês

horacifrao = float(input("Informe em Reais (R$), o valor ganho por hora: "))

htrabalhadas = float(input("Informe a quantidade de horas trabalhadas por Mês "))

salmes = horacifrao * htrabalhadas

print("O salário do mês em questão foi de {}".format(salmes))