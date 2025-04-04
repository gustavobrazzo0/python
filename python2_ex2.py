'''

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

'''

n = float(input('Insira um número: '))

if n > 0:
  print('O número informado é postivo')
elif n == 0:
    print('O número informado é 0')
else:
    print('O número informado é negativo')