'''

Faça um Programa que leia três números e mostre o maior deles.

'''

n1 = int(input('Insira o 1º número'))

n2 = int(input('Insira o 2º número'))

n3 = int(input('Insira o 3º número'))

if n1>n2 and n1>n3:
  print('o maior número é {}'.format(n1))
elif n2>n1 and n2>n3:
  print('o maior número é {}'.format(n2))
elif n3>n1 and n3>n2:
  print('o maior número é {}'.format(n3))