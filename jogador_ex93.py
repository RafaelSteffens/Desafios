desempenho = {'nome':'a', 'gols':[], 'total': 0}
total = 0

nome = str(input("Nome do jogador: "))
desempenho["nome"]  = nome
partidas = int(input(f"Quantas partidas {nome} jogou? "))

for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    desempenho["gols"].append(gols)
    total = sum(desempenho['gols'])
    desempenho["total"] = total

print('=-'*30)

print(desempenho)

print('=-'*30)

print(f'O nome tem o valor  {desempenho["nome"]}')
print(f'o campo gols tem o valor {desempenho["gols"]}')
print(f'o campo total tem o valor {total}')

print('=-'*30)

print(f'O jogador {nome} jogou {partidas}')

for i, v in enumerate (desempenho['gols']):
    print(f'    => Na partida {i} fez {v} gols. ')
 

print('=-'*30)

