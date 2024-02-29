import random
palpites = []
premio =[]
cnt=0
print('=-'*30)
print('-=-=-=-JOGO DA MEGA SENA =-=-=-=-=-')
print('=-'*30)
while True:
    jogos = int(input('Digite quantos jogos você gostaria de fazer: '))
    print(F'=-=-=- SORTEANDO {jogos} JOGOS=-=-=-=-')
    for c in range(jogos):
        for a in range(1, 6):   
            palpite = random.randint(1, 60)
            if palpite in palpites:
                cnt +=1
            else:
                palpites.append(palpite)
            
        premio.append(palpites[:])
        palpites.clear()
        premio[c].sort()
        print(f'Jogo {c}: {premio[c]}')
    print('=-=-=-=-=-BOA SORTE!!!=-=-=-=-=-')
    break


