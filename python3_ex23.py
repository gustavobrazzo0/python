'''

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

'''

def eh_primo(n):
    if n < 2:
        return False, 0
    if n == 2:
        return True, 1
    if n % 2 == 0:
        return False, 1

    divisoes = 1
    for i in range(3, int(n**0.5) + 1, 2):
        divisoes += 1
        if n % i == 0:
            return False, divisoes

    return True, divisoes

N = int(input("Escolha o número limite para saber quantas divisões são necessárias para descobri-lo primo"))
primos = []
total_divisoes = 0

for num in range(1, N + 1):
    primo, div = eh_primo(num)
    total_divisoes += div
    if primo:
        primos.append(num)

print("Números primos:", primos)
print("Total de divisões executadas:", total_divisoes)