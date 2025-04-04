'''

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são
ordenados.

Mostre os valores com uma casa decimal sem arredondar.

'''

while True:
    nome = input("Digite o nome do atleta (ou deixe em branco para sair): ").strip()
    if not nome:
        break

    saltos = []
    for i in range(5):
        salto = float(input(f"Digite a distância do {i+1}º salto: "))
        saltos.append(salto)

    melhor = max(saltos)
    pior = min(saltos)
    saltos.remove(melhor)
    saltos.remove(pior)

    media = sum(saltos) / 3

    print(f"\nAtleta: {nome}")
    print(f"Melhor salto eliminado: {melhor:.1f} m")
    print(f"Pior salto eliminado: {pior:.1f} m")
    print(f"Média dos demais saltos: {media:.1f} m\n")