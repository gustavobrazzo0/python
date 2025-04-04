'''

17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
* comprar apenas latas de 18 litros;
* comprar apenas galões de 3,6 litros;
* misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

area = float(input("Digite o tamanho da área a ser pintada (m²): "))

litros = area / 6 * 1.1  # Acrescentando 10% de folga

# Apenas latas de 18 litros
latas = int(litros / 18)
if litros % 18 != 0:
    latas += 1
custo_latas = latas * 80

# Apenas galões de 3.6 litros
galoes = int(litros / 3.6)
if litros % 3.6 != 0:
    galoes += 1
custo_galoes = galoes * 25

# Mistura de latas e galões
latas_mix = int(litros / 18)
resto = litros - (latas_mix * 18)
galoes_mix = int(resto / 3.6)
if resto % 3.6 != 0:
    galoes_mix += 1
custo_mix = (latas_mix * 80) + (galoes_mix * 25)

print(f"\nOpção 1 - Apenas latas de 18L: {latas} latas, custo R$ {custo_latas:.2f}")
print(f"Opção 2 - Apenas galões de 3.6L: {galoes} galões, custo R$ {custo_galoes:.2f}")
print(f"Opção 3 - Misturando latas e galões: {latas_mix} latas e {galoes_mix} galões, custo R$ {custo_mix:.2f}")