'''

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

'''

kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))

preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

valor_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)

total_kg = kg_morango + kg_maca
if total_kg > 8 or valor_total > 25:
    valor_total *= 0.90  

print(f"Valor a ser pago: R$ {valor_total:.2f}")