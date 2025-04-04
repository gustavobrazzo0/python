'''

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

'''

def calcular_aluno_mais_baixo_e_mais_alto(*alunos):
    if not alunos:
        return "Nenhum aluno informado."

    mais_alto = mais_baixo = alunos[0]

    for aluno in alunos:
        if aluno[1] > mais_alto[1]:
            mais_alto = aluno
        if aluno[1] < mais_baixo[1]:
            mais_baixo = aluno

    return f"O maior aluno é o {mais_alto[0]} com {mais_alto[1]} cm. O menor aluno é o {mais_baixo[0]} com {mais_baixo[1]} cm"

# Exemplo de uso
print(calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199)))
