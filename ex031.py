#Ex031 - preço da passagem de acordo com a viagem...
distância = float(input('Qual foi a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}km '.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

