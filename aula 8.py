import os

os.mkdir('Pasta esquisita')







file = open('Lista.txt','r+')
cliente = input('Digite o seu nome')
pedido = input('Digite o seu pedido')
valor = float(input('Digite o valor do pedido'))

mensagem = f'O {cliente} pediu  {pedido}, o valor total deu: {valor}'

file.write(mensagem)