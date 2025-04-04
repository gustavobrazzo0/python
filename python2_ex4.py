'''

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''

letra = str(input('Informe uma letra: '))

vogal = ['a','e','i','o','u']

if letra in vogal:
  print('VOGAL !')
else:
  print('consoante')