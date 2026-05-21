import time


servicos = ["Cronômetro", 'Temporizador']


def cronometro():
    ms = 0
    seg = 0
    min = 0
    hora = 0
    while True:
        time.sleep(0.01)
        ms+=1
        if ms>=100:
            ms=0
            seg+=1
        if seg >= 60:
            seg = 0
            min +=1
        if min >=2:
            min = 0
            hora +=1
        print(f'{hora}:{min}:{seg}:{ms}')


def relogio():
    print(servicos)
    escolhas = input('Escolha um serviço:')
    while escolhas not in servicos:
        print("Serviço não encontrado, tente escrever corretamente.")
        escolhas = input('Escolha um serviço:')





print('Escolha um serviço')
escolha = int(input('1-Despertador'  '2-Cronômetro'))


if escolha == 2:
    cronometro()