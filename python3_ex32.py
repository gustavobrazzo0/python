'''

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

'''

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    resultado = calcular_fatorial(numero)
    print(f"{numero}! = {resultado}")