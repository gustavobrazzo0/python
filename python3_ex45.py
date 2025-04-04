'''

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

'''

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas = []

while True:
    acertos = 0
    print("Responda as 10 questões:")
    for i in range(10):
        resposta = input(f"Questão {i+1}: ").strip().upper()
        if resposta == gabarito[i]:
            acertos += 1
    notas.append(acertos)

    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
    if continuar != 'S':
        break

if notas:
    maior_acerto = max(notas)
    menor_acerto = min(notas)
    total_alunos = len(notas)
    media_turma = sum(notas) / total_alunos

    print("\nResultados da turma:")
    print(f"Maior acerto: {maior_acerto}")
    print(f"Menor acerto: {menor_acerto}")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média da turma: {media_turma:.1f}")
else:
    print("Nenhum aluno respondeu à prova.")