'''
 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

'''

valor_hora = float(input("Digite o valor da sua hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

# Definição do desconto do IR
if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

ir_desconto = salario_bruto * (ir_percentual / 100)
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

total_descontos = ir_desconto + sindicato
salario_liquido = salario_bruto - total_descontos

print("Folha de Pagamento")
print(f"Salário Bruto:    R$ {salario_bruto:8.2f}")
print(f"(-) IR ({ir_percentual}%):  R$ {ir_desconto:8.2f}")
print(f"(-) Sindicato (3%): R$ {sindicato:8.2f}")
print(f"FGTS (11%):        R$ {fgts:8.2f}")
print(f"Total de descontos: R$ {total_descontos:8.2f}")
print(f"Salário Líquido:    R$ {salario_liquido:8.2f}")

