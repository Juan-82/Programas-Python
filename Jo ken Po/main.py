import extencao as ex
from random import randint


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
        ex.jogada(jogador, randint(0, 2))
    if input('Continuar [S/N]: ').strip().lower()[0] == 'n':
        break

print('Fim')