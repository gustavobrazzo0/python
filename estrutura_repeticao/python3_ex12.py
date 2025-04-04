'''

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

'''

taboo = int(input("insira o número que deseja ver a tabuada"))

for i in range(1,11):
  calc = taboo * i
  print('{} x {} = {}'.format(taboo, i, calc))