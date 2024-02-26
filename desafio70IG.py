print('''
------------------------------
      LOJA SUPER BARATÃO
------------------------------

''')
#cria o dicionário
compras = {}
continua = 's'

#executa o bloco principal
while True:
    while continua == 's':
        prod = str(input('Nome do produto: '))
        preco = float(input('Digite o valor: '))
        compras[prod] = preco #salva na biblioteca os valores
        continua = str(input('Você deseja continuar? [s/n] ? '))
    if continua == 'n': 
        print('-----------FIM DO PROGRAMA------')
        break
    else:
        print('ERROUUUU')

#calcula o valor total dos produtos do dicionário
total_compra = sum(compras.values())

#conta quantos produtos custam mais de mil
prod_caros = 0
for preco in compras.values():
    if preco > 1000:
        prod_caros += 1

#define o produto mais barato
prod_barato = min(compras, key=compras.get)
preco_baixo = compras[prod_barato]


print(f'O total de compras foi R${total_compra}')
print(f'Temos{prod_caros} que custam mais de R$1.000,00')
print(f'O produto mais barato foi {prod_barato} que custa R$ {preco_baixo}')
