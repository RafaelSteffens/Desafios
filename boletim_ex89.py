temp = []
boletim = []
media = 0
while True:
    temp.append(str(input('Digite o nome do aluno: ')))
    temp.append(int(input('Digite a 1º nota: ')))
    temp.append(int(input('Digite a 2º nota: ')))
    boletim.append(temp[:])
    temp.clear()
    
    var = str(input('Deseja continuar? [y/n] '))
    if var == 'n' or var == 'N':
        break

print('=-'*30)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-BOLETIM=-=-=-==-=-=-=-=-=--=-=-=-=')
print('=-'*30)
print('Nº   NOME        MÉDIA')

for c in range(len(boletim)):
    media = (((boletim[c][1])+(boletim[c][2]))/2)
    print(f'{c:<4}  {boletim[c][0]:<9}   {media:>7}')
    print('-'*60)

while True:
    p = int(input('Você quer saber a nota de qual aluno?  (999 interrompe)'))

    for c in range(len(boletim)):
        if p == c:
            print(f'As notas de {boletim[c][0]} são {boletim[c][1]} e {boletim[c][2]}.')

    if p == 999:
        break

print('FIM')