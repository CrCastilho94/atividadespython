from random import choice
n1 = str(input('Primeiro ALuno '))
n2 = str(input('Segundo Aluno '))
n3 = str(input('Terceiro Aluno '))
n4 = str(input('Quarto Aluno '))
lista = (n1, n2, n3, n4)
escolhido = choice(lista)
print('O Aluno escohido foi {}'.format(escolhido))

