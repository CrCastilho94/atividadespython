dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km rodado? '))
pago = (dias * 60) + (km * 0.15)
print('O valor total do alguel é de R${:.2f}'.format(pago))



