'''

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = num1 + num2
    operacao = "soma"
elif opcao == 2:
    resultado = num1 - num2
    operacao = "subtração"
elif opcao == 3:
    resultado = num1 * num2
    operacao = "multiplicação"
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: Divisão por zero não permitida.")
        exit()
else:
    print("Opção inválida!")
    exit()

par_impar = "par" if resultado % 2 == 0 else "ímpar"
positivo_negativo = "positivo" if resultado > 0 else "negativo"
inteiro_decimal = "inteiro" if resultado.is_integer() else "decimal"

print(f"Resultado da {operacao}: {resultado:.2f}")
print(f"O número é {par_impar}, {positivo_negativo} e {inteiro_decimal}.")