def titulo():
  #Impressao Titulo

  print('\033[1;33m-=' * 20, end = '')
  print('-')
  print(f'\033[1;m {"JOGO DAS VEIA!!!!":^40}')
  print('\033[1;33m-=' * 20, end = '')
  print('-\033[m')


def definindoTamV():
  #Define o tamanho do tabuleiro e o tamanho da sequência para vencer

  global tamanho, jogo, linha, coluna
  print('Digite o tamanho: ')
  while True:
    try:
      linha = int(input('Linha: '))
      coluna = int(input('Coluna: '))
      assert(linha >= 3 and coluna >= 3)
    except:
      print('\033[1;31mErro\033[m')
      continue
    else:
      if linha == 3 or coluna == 3:
        tamanho = 3
      else:
        tamanho = 4
      break
  jogo = []
  for _ in range(linha):
    s = []
    for _ in range(coluna):
      s.append(' ')
    jogo.append(s[:])


def impressao():
  #Contagem das Colunas

  print('\033[1;33m', end ='   ')
  for i in range(coluna):
    print(i, end = '   ')
  print('\n\033[m')

  #Impressao do Tabuleiro
  for i in range(linha):
    for ii in range(coluna):
      #Contagem das Linhas
      if ii == 0: print(f'\033[1;33m{i}', '  ', end='\033[m')

      print(jogo[i][ii], end ='')
      if ii != coluna-1:
        print(' | ', end ='')
      else:
        print()
    if i != linha-1:
      print('  ', '-' * 4 *coluna)
  print('\n\n')

def jogada(jogador):
  #Realiza a jogada

  print(f'Jogador {jogador}, sua vez!!!')
  while True:
    try:
      l = int(input('\033[1;33mLinha: \033[m'))
      c = int(input('\033[1;33mColuna: \033[m'))
      assert 0 <= l < linha and 0 <= c < coluna and jogo[l][c] == ' '
    except: print('\033[1;31mErro!!!\033[m')
    else: break
  if jogador == 1: jogo[l][c] = 'X'
  else: jogo[l][c] = '0'



def verColunas():
  #Verifica Colunas

  for l in jogo:
    for simbolo in 'X', '0':
      if simbolo * tamanho in ''.join(l):
        return True
  return False                  

def verLinhas():
  #Verifica linhas

  for simbolo in 'X', '0':
    for i in range(coluna):
      l = ''
      for ii in range(linha):
        l = l + jogo[ii][i]
      if simbolo * tamanho in l:
        return True
  return False


def verDiagonal():
  #Verifica Diagonal
  #Diagonal Primaria == d1
  #Diagonal Secundaria == d2

  for l in range(linha - tamanho + 1):
    for c in range(coluna - tamanho + 1):
      d1 = d2 = ''
      for i in range(tamanho):
        d1 = d1 + jogo[l + i][c + i]
        d2 = d2 + jogo[l + i][(c + 1) * (-1) - i]
      for simbolo in 'X','0':
        simbolo = simbolo * tamanho
        if simbolo in d1 or simbolo in d2:
          return True
  return False
        