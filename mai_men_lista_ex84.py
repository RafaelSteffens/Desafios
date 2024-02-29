pessoas = list()
principal =[]
cont = 0
mai = men = 0

#laço até o break
while True:
    pessoas.append(str(input("Digite seu nome: ")))
    pessoas.append(float(input("Digite seu peso: ")))
    
    if len(principal) == 0: # se a lista principal não tiver nada mai e men é quem esta inscrevendo
        mai = men = pessoas[1]

    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]

    principal.append(pessoas[:]) #salva no principal uma cópia de pessoas sem ligação e como lista com dois dados
    pessoas.clear() #limpa lista pessoas
    continuar= str(input('Deseja continuar?  [y/n]'))
    
    if continuar == 'y':
        cont += 1
    else:
        print('Finalizando...')
        cont += 1
        break

print(f'Ao todo, você cadastrou {cont}') #tambem poderia utilizar metodo len principal para saber quantos cadastros tem

print(f'E o maior peso foi de {mai} kg  do', end='')

for c in principal: # varre a lista principal sendo o c a variavel que percorre cada item
    if c[1] == mai:
        print(f'[{c[0]}]', end="")

print(f' e o menor peso foi de {men} da ', end='')
for c in principal:
    if c[1] == men:
        print(f'[{c[0]}]', end='')

