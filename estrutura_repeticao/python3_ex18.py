'''

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

'''
maior = float('-inf')
menor = float('inf')
soma = 0


n = int(input("Quantos números você deseja inserir? "))


for i in range(1, n + 1):
    numero = int(input('Insira o {}º Número: '.format(i)))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print('Do conjunto inserido, {} é o menor número, {} é o maior e a soma do conjunto resulta em: {}'.format(menor, maior, soma))
