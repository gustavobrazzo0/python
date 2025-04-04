'''

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.

'''

cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total_geral = 0
quantidade_total = 0

print("Cardápio:")
for codigo, (item, preco) in cardapio.items():
    print(f"{codigo} - {item}: R$ {preco:.2f}")

while True:
    codigo = int(input("Digite o código do item (ou -1 para finalizar): "))
    if codigo == -1:
        break
    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade: "))
        item, preco = cardapio[codigo]
        valor_item = preco * quantidade
        total_geral += valor_item
        quantidade_total += quantidade
        print(f"{item}: {quantidade} x R$ {preco:.2f} = R$ {valor_item:.2f}")
    else:
        print("Código inválido!")

print(f"Total de itens comprados: {quantidade_total}")
print(f"Total a pagar: R$ {total_geral:.2f}")

