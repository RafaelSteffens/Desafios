from random import randint
import time
from operator import itemgetter
dados = {'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6)
         }
print(f'Os jogos foram')
ranking = list()

for k, v in dados.items():
    print(f'{k} tirou {v} no dado. ')
    time.sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

print("=-"*30)
print("=-=-=-=-=-=-=- JOGADA =-=-=-=-=-==-")
print("=-"*30)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1)