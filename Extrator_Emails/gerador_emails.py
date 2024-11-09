#Gera um arquivo txt com uma lista de 5 emails gerados aleatoriamente, 
#mas se já existir ele adiciona esses emails no arquivo

from random import randint, choices
from string import ascii_letters as alfabeto
from string import digits
alfabeto += digits + '-_'
lista = []

for _ in range(5):
    email = ''.join(choices(alfabeto, k=randint(1,9))) + '@'
    for _ in range(randint(1, 4)):
        email += ''.join(choices(alfabeto, k=randint(1,9))) + '.'
    email += ''.join(choices(alfabeto, k=randint(1,9)))
    lista.append(email)

with open('emails_aleatorios.txt', 'a') as txt:
    txt.write(f'\n{"\n".join(lista)}')
print('Emails gerados com sucesso!')


    
        


