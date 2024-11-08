def titulo():
    print('\033[1;33m-=' * 20, end = '')
    print('-')
    print(f'\033[1;37m {"Jo Ken Po!!!!":^40}')
    print('\033[1;33m-=' * 20, end = '')
    print('-\033[m')


def jogada(jogador, bot):
    jogadas = 'Pedra', 'Papel', 'Tesoura'
    if jogador == bot:
        print('\033[1;37mEmpate!!!\033[m')
    else:
        for i in (0,2), (1,0), (2,1):
            if jogador == i[0] and bot == i[1]:
                print('\033[1;33mJogador Venceu!!!\033[m')
                break
        else:
            print('\033[1;31mBot Venceu!!!\033[m')
    print('\033[1;33mJogador: \033[1;37m', jogadas[jogador])
    print('\033[1;31mBot: \033[1;37m', jogadas[bot], '\033[m')