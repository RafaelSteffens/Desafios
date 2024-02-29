lista=[]

for c in range(1,6):
    escolha = (int(input(f'Digite o valor {c}: ')))
    for i, v in enumerate(lista):
        if escolha < v:
            lista.insert(i, escolha)
            break
    else:
        lista.append(escolha)


print('A lista ordenada é: ', lista)