#ex039 Alistamento Militar
from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade ==18:
      print('Você tem que se alistar IMEDIATAMENTE! Faça seu alistamento militar em: https://alistamento.eb.mil.br/  ')
elif idade < 18:
      saldo = 18 - idade
      print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento '.format(saldo))
elif idade > 18:
      saldo = idade - 18
      print('Você deveria ter se alistado ha {} anos atras'.format(saldo) )






