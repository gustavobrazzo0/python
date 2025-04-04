'''

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

'''

maior = float('-inf')
menor = float('inf')
soma = 0


n = 1000


for i in range(1, n + 1):
    numero = int(input('Insira o {}º Número: '.format(i)))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print('Do conjunto inserido, {} é o menor número, {} é o maior e a soma do conjunto resulta em: {}'.format(menor, maior, soma))