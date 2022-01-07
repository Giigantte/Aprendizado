from random import choice
from time import sleep
print('Bom dia')
sleep(1)
jogar = input('Quer jogar? ')
if jogar == 'sim':
  print('Então vamos la, Pedra, Papel e Tesoura então! ')
  sleep(1)
  pergunta = input('Escolha o seu: ')
  lista = ['Pedra', 'Papel', 'Tesoura']
  sorteio = choice(lista)
#PEDRA
  if pergunta == 'Pedra' and sorteio == 'Tesoura':
    print('Eu escolhi {} e você escolheu {}. Você ganhou'.format(sorteio, pergunta))
  elif pergunta == 'Pedra' and sorteio == 'Pedra':
    print('Eu escolhi {} e você escolheu {}. Empatamos'.format(sorteio, pergunta))
  elif pergunta == 'Pedra' and sorteio == 'Papel':
    print('Eu escolhi {} e você escolheu {}. Eu ganhei'.format(sorteio, pergunta))
#PAPEL
  elif pergunta == 'Papel' and sorteio == 'Tesoura':
    print('Eu escolhi {} e você escolheu {}. Eu ganhei'.format(sorteio, pergunta))
  elif pergunta == 'Papel' and sorteio == 'Papel':
    print('Eu escolhi {} e você escolheu {}. Empatamos'.format(sorteio, pergunta))
  elif pergunta == 'Papel' and sorteio == 'Pedra':
    print('Eu escolhi {} e você escolheu {}. Você ganhou'.format(sorteio, pergunta))
#TESOURA
  elif pergunta == 'Papel' and sorteio == 'Tesoura':
    print('Eu escolhi {} e você escolheu {}. Você ganhou'.format(sorteio, pergunta))
  elif pergunta == 'Papel' and sorteio == 'Pedra':
    print('Eu escolhi {} e você escolheu {}. Empatamos'.format(sorteio, pergunta))
  elif pergunta == 'Papel' and sorteio == 'Papel':
    print('Eu escolhi {} e você escolheu {}. Eu ganhei'.format(sorteio, pergunta))
else:
  print('Tudo bem, obrigado mesmo assim')
