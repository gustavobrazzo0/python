'''

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.

'''

n = int(input("Insira o número de termos da série de Fibonacci: "))

a, b = 1, 1
serie = []

if n >= 1:
    serie.append(a)
if n >= 2:
    serie.append(b)

for _ in range(2, n):
    a, b = b, a + b
    serie.append(b)

print(f"A série de Fibonacci até o {n}-ésimo termo é: {serie}")