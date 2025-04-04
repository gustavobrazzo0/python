'''

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e
seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes

'''

clientes = []

while True:
    nome = input("Nome (ou 0 para sair): ")
    if nome == "0":
        break
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    clientes.append((nome, altura, peso))

if clientes:
    mais_alto = clientes[0]
    mais_baixo = clientes[0]
    mais_gordo = clientes[0]
    mais_magro = clientes[0]
    soma_altura = 0
    soma_peso = 0

    for cliente in clientes:
        nome, altura, peso = cliente
        soma_altura += altura
        soma_peso += peso

        if altura > mais_alto[1]:
            mais_alto = cliente
        if altura < mais_baixo[1]:
            mais_baixo = cliente
        if peso > mais_gordo[2]:
            mais_gordo = cliente
        if peso < mais_magro[2]:
            mais_magro = cliente

    media_altura = soma_altura / len(clientes)
    media_peso = soma_peso / len(clientes)

    print(f"Mais alto: {mais_alto[0]} ({mais_alto[1]:.2f}m)")
    print(f"Mais baixo: {mais_baixo[0]} ({mais_baixo[1]:.2f}m)")
    print(f"Mais gordo: {mais_gordo[0]} ({mais_gordo[2]:.1f}kg)")
    print(f"Mais magro: {mais_magro[0]} ({mais_magro[2]:.1f}kg)")
    print(f"Média altura: {media_altura:.2f}m, Média peso: {media_peso:.1f}kg")
else:
    print("Nenhum cliente registrado.")

