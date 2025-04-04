'''

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

'''

divida = float(input("Digite o valor da dívida: "))
parcelas_juros = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

print("Quantidade de Parcelas | % de Juros | Valor dos Juros | Valor Total | Valor da Parcela")
print("-" * 80)

for qtd_parcelas, juros in parcelas_juros:
    valor_juros = divida * (juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas
    print(f"{qtd_parcelas:^22} | {juros:^10} | R$ {valor_juros:^12.2f} | R$ {valor_total:^10.2f} | R$ {valor_parcela:^12.2f}")