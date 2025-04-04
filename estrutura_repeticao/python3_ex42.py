'''

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

'''

contagem = [0, 0, 0, 0]

while True:
    numero = int(input("Digite um número positivo (ou negativo para sair): "))
    if numero < 0:
        break
    elif 0 <= numero <= 25:
        contagem[0] += 1
    elif 26 <= numero <= 50:
        contagem[1] += 1
    elif 51 <= numero <= 75:
        contagem[2] += 1
    elif 76 <= numero <= 100:
        contagem[3] += 1

print("Contagem de números por intervalo:")
print(f"[0-25]: {contagem[0]}")
print(f"[26-50]: {contagem[1]}")
print(f"[51-75]: {contagem[2]}")
print(f"[76-100]: {contagem[3]}")