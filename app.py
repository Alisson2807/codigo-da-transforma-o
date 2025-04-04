print('ola mundo')
print('gosto de jogar bola')
print('eu so da bahia')
caixa='abacate'

print(caixa)

nome='alisson'
idade=16
altura=1.78
estudante=True

print(nome,idade,altura,estudante)

mensagem='bem vindo ao fut de cria'
print(mensagem.strip())
print(mensagem.upper())
print(mensagem.lower())

nome=input('qual e o seu nome?')
print(f'ola {nome},seja muito bem vindo ao codigo da transformação')

from datetime import datetime

nome= input('qual e o seu nome')
agora= datetime.now()
hora_atual = agora.strftme('%H:%M')
print(f'ola,{nome}!agora são {hora_atual}')