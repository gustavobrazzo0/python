'''

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

'''

print ("informe seu gênero e altura para saber seu peso ideal")

gender = str(input("Se você é homem digite h, se você é mulher digite m: "))

altura = float(input("informe sua altura para saber seu peso ideal: "))

if gender == "h":
  phomem= (72.7 * altura) - 58
  print(" Seu peso ideal é de {}".format(phomem))

if gender == "m":
  pmulher= (62.1 * altura) - 44.7
  print(" Seu peso ideal é de {}".format(pmulher))

else:
  print("valor informado está incorreto !")