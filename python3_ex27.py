'''

Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.

'''


import math

T = int(input("Digite a quantidade de turmas: "))
alunos_total = 0

for i in range(T):
    while True:
        alunos = int(input(f"Digite a quantidade de alunos na turma {i+1} (entre 1 e 40): "))
        if 1 <= alunos <= 40:
            alunos_total += alunos
            break
        else:
            print("Quantidade inválida! Insira um número entre 1 e 40.")

media = math.floor(alunos_total / T)
print(f"O número médio de alunos por turma é: {media}")