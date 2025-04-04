'''

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

area = float(input('Informe a àrea à ser pintada em metros: '))

tinta_usd = area / 3

latas_usd = tinta_usd / 18

preço_total = latas_usd * 80

print('são necessárias {} latas para pintar uma àrea de {} metros, resultando num preço total de {}'.format(latas_usd, area, preço_total))