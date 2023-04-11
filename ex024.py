nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome... ')
print('Seu nome em maísculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} Letras'.format(len(nome) - nome.count(' ')))
#print('Seu nome primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


