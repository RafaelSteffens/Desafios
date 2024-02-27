#EXERCICIO 78 DO CURSO EM VIDEO

lista = []
mai = men = 0

for c in range(0,6):
    lista.append(float(input('Digite um número: '))) #função input já salvando na lista
    if c == 0:
        mai=men=lista[c] 

    else:
        if lista[c] > mai: # lista[c] faz referência no item da lista que o for esta lendo no momento
            mai = lista[c] #atribui a variavel 'mai' o item da lista que o for esta lendo em 'c'

        if lista[c] < men:#ler comentários acima
            men = lista[c]

print(f'Voce digitou os valores {lista}')
#maior = max(lista)
#menor = min(lista)
print(f'O maior valor digitado foi {mai} ', end='')

for p,v in enumerate(lista): #estrutura for aonde 'p' é a posição, 'v' é o valor, enumerate é a função que mostra as duas variaveis da lista
    if v == mai:  #se o "v"  analisado no momento for igual a variavel mai ele mostra a posição, end=' é para não quebrar a linha
        print(f'{p}...', end='')


print(f'O menor valor digitado foi {men} ', end='')
for p, v in enumerate(lista):   
    if v == men:   #se o "v"  analisado no momento for igual a variavel men ele mostra a posição, end=' é para não quebrar a linha
        print(f'{p}...')

