'''

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

Mostre os valores monetórios com duas casas decimais.

'''

N = int(input("Digite a quantidade de CDs na coleção: "))

total_investido = 0

for i in range(N):
    valor = float(input(f"Digite o valor do CD {i+1}: "))
    total_investido += valor

media = total_investido / N

print(f"Valor total investido: R$ {total_investido:.2f}")
print(f"Valor médio gasto por CD: R$ {media:.2f}")