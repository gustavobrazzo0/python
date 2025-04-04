'''

Altere o programa anterior para mostrar no final a soma dos números.

'''

num1 = int(input('Insira o primeiro número'))

num2 = int(input('Insira o segundo número'))

soma = num1 + num2

if num1 < num2:
  for i in range (num1+ 1, num2):
    print(i)
elif num2 < num1:
    for i in range(num2+ 1, num1):
      print(i)
else:
  print('os números são iguais não há intervalo entre eles')

print('A soma dos dois números é {}'.format(soma))