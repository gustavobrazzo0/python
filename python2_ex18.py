'''

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

'''

dia, mes, ano = map(int, input("Digite uma data (dd/mm/aaaa): ").split("/"))

if (1 <= mes <= 12) and (1 <= dia <= 31):
    if mes in {4, 6, 9, 11} and dia > 30:
        print("Data inválida.")
    elif mes == 2 and dia > 29:
        print("Data inválida.")
    elif mes == 2 and dia == 29 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
        print("Data inválida.")
    else:
        print("Data válida.")
else:
    print("Data inválida.")