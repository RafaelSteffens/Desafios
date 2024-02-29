desempenho = dict()
gols = list()
lista = []
total = 0

while True:
    desempenho.clear()
    gols.clear()
    nomes = str(input("Nome do jogador: "))
    desempenho["nome"]  = nomes
    partidas = int(input(f"Quantas partidas {nomes} jogou? "))
    desempenho['partidas'] = partidas
    total = 0
    
    for c in range(partidas):
        gol =(int(input(f'Quantos gols na partida {c}? ')))
        gols.append(gol)
        total += gol
    desempenho["total"] = total
    desempenho["gols_partida"] = gols[:]
    lista.append(desempenho.copy())

    while True:

        cont = str(input('Quer continuar[y/n]')).upper()[0]
        if cont in 'YN':
            break
        print('ERROUUU! Responda apenas y ou n')
    if cont == 'N':
            break

print('=-'*30)

print(lista)
for c , d in enumerate(lista):
    print(f' O jogador {c} foi salvo com {d}')

print('=-'*30)

while True:
    escolha = int(input(f'Qual jogador você deseja ver as estatisticas? (999 para parar) '))
    for c in range(len(lista)):
        if c == escolha:
            cnome = lista[c]["nome"]
            cgols =lista[c]["gols_partida"]
            ctotal = lista[c]["total"]
            cpartidas = len(lista[c]['gols_partida'])
            print(f'O nome tem o valor  {cnome}')
            print(f'o campo gols tem o valor {cgols}')
            print(f'o campo total tem o valor {ctotal}')

            print('=-'*30)

            print(f'O jogador {cnome} jogou {cpartidas} jogos')

            for i, d in enumerate (lista[c]['gols_partida']):
                print(f'    => Na partida {i} fez {d} gols. ')
        if escolha == 999:
            break    

            print('=-'*30)

