'''

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas

'''

peso = float(input("Informe o peso da última pesca:"))

kgex = peso - 50

if kgex > 0:
  multa = kgex * 4
  print ("você excedeu o peso limite em {} kgs, então devera pagar {} R$ de multa.".format(kgex, multa))

else:
  print("Você não excedeu o peso limite, portanto não pagará multa")
