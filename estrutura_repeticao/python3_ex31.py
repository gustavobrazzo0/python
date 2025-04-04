'''

O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
Um valor -1 deve ser informado pelo operador para finalizar o programas
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.

'''

while True:
    total_compra = 0
    print("\nNova compra iniciada. Digite os preços dos produtos (0 para finalizar compra, -1 para sair):")

    while True:
        preco = float(input("Digite o preço do produto: "))

        if preco == -1:
            print("Encerrando o programa...")
            exit()
        elif preco == 0:
            break
        else:
            total_compra += preco

    print(f"Total da compra: R$ {total_compra:.2f}")

    dinheiro = float(input("Digite o valor pago pelo cliente: "))
    troco = dinheiro - total_compra
    print(f"Troco: R$ {troco:.2f}")