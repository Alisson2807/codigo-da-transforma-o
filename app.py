print("Ola mundo")

caixa='caneta' 
 
print (caixa)

nome='carlos'
idade= 18
altura= 1.70
estudante= True

print(f'nome:{nome}, idade: {idade}, altura: {altura}, estudante: {estudante}')

mensagem = "python e divertido" 

print(mensagem.strip())
print(mensagem.lower())
print(mensagem.upper())

nome = input("qual o seu nome? ")
print(f'Ola {nome}, seja bem vindo')

from datetime import datetime

nome = input("qual e o seu nome? ")
agora = datetime.now()
hora_atual= agora.strftime("%H:%M")
print(f'Ola, {nome}! agora sao {hora_atual}.')
