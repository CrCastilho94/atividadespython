#Mundo 02 Python Ex036
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
casa = float(input('Valor da casa R$ '))
salario = float(input('Salario do comprador R$ '))
anos = int(input('Quantos anos do financiamento '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de  R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO! ')
