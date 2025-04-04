'''

Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

'''

sexo = str(input('Informe o sexo (f para feminino e m para masculino): '))

if sexo == 'f' or sexo == 'm':
  print('Ok !')
else:
  print('Sexo inválido !')