'''

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

'''

n = int(input('Insira o número para verificação: '))

if n <= 1:
    print('O número não é primo.')
else:
    primo = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print('O número é primo.')
    else:
        print('O número não é primo.')