'''

Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
1) Esse funcionário foi contratado em 2018;
2) Em 2019 recebeu aumento de 1,5% sobre seu salário inicial;
3) A partir de 2020 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine a evolução salarial do funcionário em 5 anos

Os valores devem ser exibidos com duas casas decimais

'''

salario_inicial = float(input("Digite o salário inicial do funcionário: "))
ano_contratacao = 2018
anos_trabalhados = 5
salario = salario_inicial
percentual_aumento = 1.5 / 100  # 1,5% em 2019

print(f"Ano {ano_contratacao}: R$ {salario:.2f}")

for ano in range(ano_contratacao + 1, ano_contratacao + anos_trabalhados + 1):
    salario += salario * percentual_aumento
    print(f"Ano {ano}: R$ {salario:.2f}")
    percentual_aumento *= 2  # O aumento dobra a cada ano