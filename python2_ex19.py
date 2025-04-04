'''

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

'''

numero = int(input("Digite um número inteiro menor que 1000: "))

if 0 <= numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []
    if centenas > 0:
        partes.append(f"{centenas} centena" + ("s" if centenas > 1 else ""))
    if dezenas > 0:
        partes.append(f"{dezenas} dezena" + ("s" if dezenas > 1 else ""))
    if unidades > 0:
        partes.append(f"{unidades} unidade" + ("s" if unidades > 1 else ""))

    print(f"{numero} = {', '.join(partes[:-1]) + (' e ' + partes[-1] if len(partes) > 1 else partes[0])}")
else:
    print("Número inválido! Digite um número entre 0 e 999.")