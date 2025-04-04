'''

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

'''

candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

total_votos = 0

print("Candidatos:")
for codigo, nome in candidatos.items():
    print(f"{codigo} - {nome}")
print("5 - Voto Nulo")
print("6 - Voto em Branco")

while True:
    voto = int(input("Digite o código do voto (0 para encerrar): "))
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
        total_votos += 1
    else:
        print("Código inválido!")

print("\nResultado da eleição:")
for codigo, nome in candidatos.items():
    print(f"{nome}: {votos[codigo]} votos")

print(f"Votos Nulos: {votos[5]}")
print(f"Votos em Branco: {votos[6]}")

porcentagem_nulos = (votos[5] / total_votos) * 100 if total_votos > 0 else 0
porcentagem_brancos = (votos[6] / total_votos) * 100 if total_votos > 0 else 0

print(f"Percentual de votos nulos: {porcentagem_nulos:.2f}%")
print(f"Percentual de votos em branco: {porcentagem_brancos:.2f}%")
