#etrutras de repetição/laços de repetição

import time


for m in range(1,21):
    print(m)


for i in range(1,50):
    if i %2 == 0:
        print(i)



tabuada = int(input('Digite um número'))

for i in range(1,11):
    print(i*tabuada)

senha = 0000
digite = ''
while digite != senha:
    digite = int(input('Digite a senha'))
    if digite != senha:
        print('Senha incorreta')
    else:
        print('Senha correta')

numelro = 0

while numelro < 100:
    print(numelro)
    numelro +=1
    time.sleep(2)





































































