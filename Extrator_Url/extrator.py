import re

print('\033[1;33m-=' * 20, end = '')
print('-')
print(f'\033[1;37m {"Extrator de Url":^40}')
print('\033[1;33m-=' * 20, end = '')
print('-\033[m')

caminho = input('Digite o caminho do arquivo txt: ')
try:
    with open(caminho, 'r') as txt:
        padrao = re.compile(r'https?://([\w-]+\.)+[\w-]+')
        for linha in txt:
            for c in padrao.finditer(linha):
                print(c.group(0))
except:
    print('\033[1;31mErro!!!\033[m')
    print(f'O arquivo \'{caminho}\' não encontrado.')
finally:
    print('\033[1;33mFim.\033[m')