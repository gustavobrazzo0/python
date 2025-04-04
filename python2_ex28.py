'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

'''

# Exibe opções de carnes
print("Escolha o tipo de carne:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

# Entrada do tipo de carne
opcao = int(input("Digite o número da opção desejada: "))

# Entrada da quantidade de carne
quantidade = float(input("Digite a quantidade de carne (Kg): "))

# Definição de preços
if opcao == 1:
    tipo_carne = "Filé Duplo"
    preco_kg = 4.90 if quantidade <= 5 else 5.80
elif opcao == 2:
    tipo_carne = "Alcatra"
    preco_kg = 5.90 if quantidade <= 5 else 6.80
elif opcao == 3:
    tipo_carne = "Picanha"
    preco_kg = 6.90 if quantidade <= 5 else 7.80
else:
    print("Opção inválida! Tente novamente.")
    exit()

# Calcula o valor total da compra
valor_total = quantidade * preco_kg

# Pergunta sobre o pagamento no Cartão Tabajara
cartao_tabajara = input("Pagamento no Cartão Tabajara? (S/N): ").strip().upper()

# Calcula o desconto
desconto = 0
if cartao_tabajara == "S":
    desconto = valor_total * 0.05

# Valor final a pagar
valor_final = valor_total - desconto

# Exibe o cupom fiscal
print("\n===== CUPOM FISCAL =====")
print(f"Tipo de Carne: {tipo_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço por Kg: R$ {preco_kg:.2f}")
print(f"Preço Total: R$ {valor_total:.2f}")
print(f"Tipo de Pagamento: {'Cartão Tabajara' if cartao_tabajara == 'S' else 'Dinheiro/Outro'}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_final:.2f}")
print("========================")