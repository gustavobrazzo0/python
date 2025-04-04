'''

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo . a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

'''

nit1 = int(input("Informe o primeiro número inteiro"))

nit2 = int(input("Informe o segundo número inteiro"))

rl = float(input("Informe o número real"))

q1 = (nit1 * 2) * (nit2/2)

q2 = (nit1 * 3) + rl

q3 = rl**3

print ("o produto do dobro do primeiro com metade do segundo {} . a soma do triplo do primeiro com o terceiro {}. o terceiro elevado ao cubo{}.".format(q1, q2, q3))