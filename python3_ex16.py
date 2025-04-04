'''

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.

'''

a, b = 0, 1
serie = []

while b <= 500:
    serie.append(b)
    a, b = b, a + b

print(f"A série de Fibonacci até que o valor seja maior que 500 é: {serie}")