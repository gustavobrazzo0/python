'''

Altere o programa de cálculo do fatorial, 
permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

'''

while True:
  resp = input('Deseja fatoriar? ')

  if resp == 's':
    n = int(input('Insira qual número deseja fatoriar: '))

    fatorial = 1
    for i in range (1, n+ 1):
      fatorial *= i

    print('O fatorial de {} é {}'.format(n, fatorial))
  elif resp == 'n':
    break

    print('Programa Encerrado.')
  else:
    print('Opção Inválida')