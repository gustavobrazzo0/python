'''

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.

'''

nome = str(input("Insira seu nome de usuário "))
senha = str(input("Insira sua senha "))

if nome == senha:
  print("A senha não pode ser igual ao nome de usuário")
  nome = str(input("Insira seu nome de usuário "))
  senha = str(input("Insira sua senha "))
else:
  print("Cadastrado com sucesso !")