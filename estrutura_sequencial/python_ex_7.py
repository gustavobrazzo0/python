'''

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''

lado = float(input("informe a medida do lado do quadrado, que deseja saber a àrea: "))

area = lado * lado

dbarea = area * 2

print("O dobro da área do quadrado com o lado informado é {}".format(dbarea))