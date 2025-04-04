'''

Faça um programa que leia 5 números e informe o maior número.

'''

n = 0
maior = None
for i in range(1,6):
  n = int(input("Insira o {}º número: ".format(i)))
  if maior is None or n > maior:
        maior = n

print(maior)