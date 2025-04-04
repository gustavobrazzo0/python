'''

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
    
    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | H = 2.283333333333333           |
    ----------------------------------

'''

n = int(input("Digite o número de termos (N): "))

h = 0

for i in range(1, n + 1):
    h += 1 / i

print(f"H = {h}")


