'''

O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de
quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o
valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na
tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
preços de 1 até 50 produtos.

'''

preco_unitario = 1.99
quantidade_max = 50

print("Quantidade de Itens | Valor a Pagar")
print("--------------------|--------------")

for quantidade in range(1, quantidade_max + 1):
    valor_total = quantidade * preco_unitario
    print(f"{quantidade:18} | R$ {valor_total:.2f}")