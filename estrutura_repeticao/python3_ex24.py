'''

Faça um programa que calcule o mostre a média aritmética de N notas.

'''

N = int(input("Quantas notas deseja inserir? "))
notas = []

for i in range(N):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / N
print(f"A média aritmética das notas é: {media:.2f}")
