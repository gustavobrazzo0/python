'''

Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;

Idade: entre 0 e 150;

Salário: maior que zero;

Sexo: 'f' ou 'm';

Estado Civil: 's', 'c', 'v', 'd';

'''

nome = str(input("Insira seu nome de usuário: "))
idade = int(input("Insira sua Idade "))
salario = int(input("Insira seu salário "))
sexo = str(input("Insira seu sexo: (M ou F)"))
estado_civil = str(input("Insira seu estado civil: (s, c, v, d)"))

nome_tamanho = len(nome)

if nome_tamanho > 3:
  print("Nome: {},1 CHECK < OK >".format(nome))
else:
  print("Nome: {}, CHECK < X >".format(nome))

if idade > 0 and idade < 150:
  print("Idade: {}, CHECK < OK >".format(idade))
else:
  print("Idade: {}, CHECK < X >".format(idade))

if salario > 0:
  print("Salário: {}, CHECK < OK >".format(salario))
else:
  print("Salário: {}, CHECK < X >".format(salario))

if sexo == "f" or sexo == "m":
  print("Sexo: {}, CHECK < OK >".format(sexo))
else:
  print("Sexo: {}, CHECK < X >".format(sexo))

if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
  print("Estado Civil: {}, CHECK < OK >".format(estado_civil))
else:
  print("Estado Civil: {}, CHECK < X >".format(estado_civil))