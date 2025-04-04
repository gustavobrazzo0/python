'''

Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.

Mostre a média de idade com uma casa decimal.

'''

N = int(input("Quantas pessoas há na turma? "))
idades = []

for i in range(N):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)

media_idade = sum(idades) / N

if media_idade <= 25:
    classificacao = "jovem"
elif media_idade <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

print(f"A média de idade da turma é {media_idade:.1f} anos, classificando-a como {classificacao}.")