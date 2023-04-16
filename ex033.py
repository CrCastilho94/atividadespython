#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo Valor: '))
terceiro = int(input('Terceiro valor: '))
#verificando quem é o menor valor:
menor = primeiro
if segundo<primeiro and segundo<terceiro:
    menor = segundo
if terceiro<primeiro and terceiro<segundo:
        menor = terceiro
print('O menor valor digitado foi {}'.format(menor))

