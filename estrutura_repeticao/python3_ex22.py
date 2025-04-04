'''

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

'''

n = int(input('Insira o número para verificação: '))

div = n

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