'''

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

'''

cidades = []

for _ in range(5):
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio (1999): "))
    acidentes = int(input("Número de acidentes com vítimas (1999): "))
    cidades.append((codigo, veiculos, acidentes))

maior_indice = cidades[0]
menor_indice = cidades[0]
soma_veiculos = 0
soma_acidentes_menos_2000 = 0
contagem_menos_2000 = 0

for cidade in cidades:
    codigo, veiculos, acidentes = cidade
    soma_veiculos += veiculos

    if acidentes > maior_indice[2]:
        maior_indice = cidade
    if acidentes < menor_indice[2]:
        menor_indice = cidade

    if veiculos < 2000:
        soma_acidentes_menos_2000 += acidentes
        contagem_menos_2000 += 1

media_veiculos = soma_veiculos / 5
media_acidentes_menos_2000 = soma_acidentes_menos_2000 / contagem_menos_2000 if contagem_menos_2000 > 0 else 0

print(f"Maior índice de acidentes: {maior_indice[2]} (Cidade {maior_indice[0]})")
print(f"Menor índice de acidentes: {menor_indice[2]} (Cidade {menor_indice[0]})")
print(f"Média de veículos nas cidades: {media_veiculos:.1f}")
print(f"Média de acidentes em cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.1f}")
