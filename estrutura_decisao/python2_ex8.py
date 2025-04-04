'''

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato. Mostrar o resultado com duas casas decimais

'''

produto1 = float(input("Qual o valor do 1º Produto? "))
produto2 = float(input("Qual o valor do 2º Produto? "))
produto3 = float(input("Qual o valor do 3º Produto? "))

menor_preco = min(produto1, produto2, produto3)
produtos_baratos = []

if produto1 == menor_preco:
    produtos_baratos.append("Produto 1")
if produto2 == menor_preco:
    produtos_baratos.append("Produto 2")
if produto3 == menor_preco:
    produtos_baratos.append("Produto 3")

print(f"Você deve comprar: {', '.join(produtos_baratos)}, com o valor de R$ {menor_preco:.2f}")