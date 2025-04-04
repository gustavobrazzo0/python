'''

Calcule o fatorial de um número:

'''

numero = int(input('Digite o número que deseja fatoriar: '))

fatorial = numero
contador = 1

while (numero-contador)>1:
  fatorial = fatorial*(numero-contador)
  contador += 1
print('{}! = {}'.format(numero,fatorial))