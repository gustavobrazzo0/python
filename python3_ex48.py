'''

Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  entrada => 12376489
  saida => 98467321

'''

num = input("Digite um número inteiro positivo: ")

if num.isdigit():
    invertido = ""
    for caractere in num:
        invertido = caractere + invertido
    print("Número invertido:", invertido)
else:
    print("Entrada inválida. Digite um número inteiro positivo.")