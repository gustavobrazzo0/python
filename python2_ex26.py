'''

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.

Mostre o restultado com duas casas decimais

'''

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

preco_alcool = 1.90
preco_gasolina = 2.50

desconto = 0

if tipo == "A":
    preco_litro = preco_alcool
    desconto = 0.03 if litros <= 20 else 0.05
elif tipo == "G":
    preco_litro = preco_gasolina
    desconto = 0.04 if litros <= 20 else 0.06
else:
    print("Tipo de combustível inválido!")
    exit()

valor_bruto = litros * preco_litro
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print(f"Valor a ser pago: R$ {valor_final:.2f}")