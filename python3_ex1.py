'''

Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

nota = int(input("Informe um número de 0 à 10 "))

if nota >= 0 and nota <= 10:
  print("Obrigado !")
else:
   nota = int(input("Informe um número de 0 à 10 "))