'''

Em uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

'''

N = int(input("Digite o número total de eleitores: "))

votos = [0, 0, 0]  # Índices para os três candidatos

for i in range(N):
    voto = int(input(f"Eleitor {i+1}, vote no candidato 1, 2 ou 3: "))
    if voto in [1, 2, 3]:
        votos[voto - 1] += 1
    else:
        print("Voto inválido! Não será contabilizado.")

print("Resultado da eleição:")
for i, v in enumerate(votos, start=1):
    print(f"Candidato {i}: {v} votos")

