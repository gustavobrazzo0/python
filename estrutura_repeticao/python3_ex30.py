'''

O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
até 50 pães, a partir do preço do pão informado pelo usuário

'''

preco_pao = float(input("Informe o preço do pão: "))
quantidade_max = 50

print("Quantidade de Pães | Valor a Pagar")
print("-------------------|--------------")

for quantidade in range(1, quantidade_max + 1):
    valor_total = quantidade * preco_pao
    print(f"{quantidade:17} | R$ {valor_total:.2f}")