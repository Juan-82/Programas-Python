import extencao as ex
from os import system

#Definindo o tamanho de vitoria e as dimensões do tabuleiro
ex.definindoTamV()
jogador = 2

#Inicio do Jogo
for _ in range(ex.coluna * ex.linha):
  jogador = 2 if jogador == 1 else 1
  ex.titulo()
  ex.impressao()
  ex.jogada(jogador)
  system('cls')
  if ex.verColunas() or ex.verLinhas() or ex.verDiagonal():
    break

#Fim do jogo
ex.titulo()
ex.impressao()
print(f'\033[1;33mJogador {jogador} Venceu!!!! \033[m')
print('Fim')