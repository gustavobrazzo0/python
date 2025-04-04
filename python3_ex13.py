'''

Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.

'''

base = int(input('Insira a base do expoente: '))

expo = int(input('Insira o expoente da base: '))

potencia = 1

for _ in range(expo):
  potencia *= base

print('{}'.format(potencia))