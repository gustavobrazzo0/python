'''

Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

'''

numero = int(input("Digite um número para a tabuada: "))
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

if fim < inicio:
    print("Erro: O valor final não pode ser menor que o inicial.")
else:
    print(f"Tabuada de {numero} de {inicio} até {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")