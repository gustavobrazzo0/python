'''

Faça um Programa que leia três números e mostre-os em ordem decrescente.

'''

numeros = []

for i in range(3):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

numeros.sort(reverse=True)

print("Números em ordem decrescente:", numeros)