'''

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.

'''

popA = int(input("Insira a população inicial de A: "))

popB = int(input("Insira a população inicial B: "))

txA = float(input("Insira a taxa de crescimento de A: "))

txB = float(input("Insira a taxa de crescimento de B: "))

anos = 0


print(" CHECAGEM DE TIPOS ")
if type(popA) == int:
  print("CHECK < OK >".format(popA))
else:
  print("CHECK < OK >".format(popA))

if type(popB) == int:
  print("CHECK < OK >".format(popB))
else:
  print("CHECK < OK >".format(popB))

if type(txA) == float:
  print("CHECK < OK >".format(txA))
else:
  print("CHECK < OK >".format(txA))

if type(txB) == float:
  print("CHECK < OK >".format(txB))
else:
  print("CHECK < OK >".format(txB))

while popA < popB:

  popA += popA * txA
  popB += popB * txB
  anos += 1

print ("A quantidade de anos necessária para a população de A ultrapassar a População de B é: {} ".format(anos))