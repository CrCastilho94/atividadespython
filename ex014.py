salario = float(input('Qual o salario do funcionario R$: '))
novo = salario + (salario * 15/ 100)
print('O funcionario que recebia R${:.2f} \ncom 15% de aumento passara a receber R${:.2f}'.format(salario, novo))

