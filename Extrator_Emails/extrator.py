import re

print('\033[1;33m-=' * 20, end = '')
print('-')
print(f'\033[1;m {"Extrator de Email":^40}')
print('\033[1;33m-=' * 20, end = '')
print('-\033[m')

while True:
	caminho = input('Digite o caminho para o arquivo de texto: ').strip()
	try:
		with open(caminho, 'r') as texto:
			padrao = re.compile(r'([\w-]+@)([\w-]+\.)+([\w-]+)')
			for linha in texto:
				for ocorrencia in padrao.finditer(linha):
					print(ocorrencia[0])
	except:
		print('\033[1;31mErro!\033[m')
		print(f'Arquivo \'{caminho}\' não encontrado.')

	finally:
		print('\033[1;33m=-\033[m' * 15)
		if input('Quer continuar usando o programa [S/N]? ').strip().lower()[0] == 'n':
			break

print('Fim do programa.')