real = float(input('Quanto dinheiro você tem em sua carteira: R$'))
dolar = real / 5.06
euro = real / 5.51
print('Com R${:.2f} você pode comprar U$${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €$${:.2f}'.format(real, euro))



