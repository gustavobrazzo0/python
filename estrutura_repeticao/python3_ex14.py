'''

Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

'''

numeros = []
impar = 0
par = 0

for i in range(1,11):
  numero =int(input('Insira o {}º Número: '.format(i)))
  numeros.append(numero)
  if numero % 2 == 0:
    par += 1
  else:
    impar += 1

print("Os números inseridos foram: {}, {} valores pares e {} valores ímpares".format(numeros, par, impar))