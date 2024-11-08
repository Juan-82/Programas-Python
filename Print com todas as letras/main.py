from os import system
from time import sleep
from string import ascii_lowercase as alfabeto

def titulo():
    print('\033[1;33m-=' * 14)
    print('\033[1;37mPrint com Todas as Letras!!!')
    print('\033[1;33m-=\033[m' * 14)

alfabeto += ' '

while True:
    titulo()
    frase = input('Digite a frase: ').split().lower()
    frase2 = ''
    for i in frase:
        for ii in alfabeto:
            print(frase2 + ii)
            sleep(0.1)
            if i == ii:
                frase2 += ii
                break
    if input('Sair? [S/N]: ').split()[0].lower() == 's':
        break
    system('cls')