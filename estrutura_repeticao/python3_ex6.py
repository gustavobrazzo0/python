'''

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.

'''

numeros = list(range(1,21))

print(' '.join(map(str, numeros)))