'''

Faça um programa que mostre os n termos da Série a seguir:
    
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
    
    Imprima no final a soma da série.

'''

n = int(input("Digite o número de termos da série: "))

soma = 0
denominador = 1

for i in range(1, n + 1):
    soma += i / denominador
    denominador += 2

print(f"Soma da série: {soma:.2f}")