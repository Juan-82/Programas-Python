import extencao as ex
from random import randint
from time import sleep

while True:
    ex.titulo()
    print('''Digite sua jogada: 
[0] Pedra
[1] Papel
[2] Tesoura''')
    try:
        jogador = int(input('>>>').strip())
        assert (0 <= jogador <= 2)
    except:
        print('Erro, digite apenas os numeros indicados!')
    else:

        for msg in 'Jo, ', 'Ken, ', 'Po!!!':
            print('\033[1;33m' + msg, end='', flush=True)
            sleep(1)
        print('\033[m\n')
        ex.jogada(jogador, randint(0, 2))
    if input('Continuar [S/N]: ').strip().lower()[0] == 'n':
        break

print('Fim')