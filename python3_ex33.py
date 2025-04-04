''''

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

'''

temperaturas = []

while True:
    try:
        temp = float(input("Digite uma temperatura (ou 'sair' para finalizar): "))
        temperaturas.append(temp)
    except ValueError:
        break

if temperaturas:
    print(f"Menor temperatura: {min(temperaturas):.1f}°C")
    print(f"Maior temperatura: {max(temperaturas):.1f}°C")
    print(f"Média das temperaturas: {sum(temperaturas)/len(temperaturas):.1f}°C")
else:
    print("Nenhuma temperatura foi informada.")