matrix=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0


for l in range(0,3): #para cada linha 'l' de 0 a 3
    for c in range(0, 3): #para cada coluna 'c' de 0 a 3
        matrix[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #adiciona um valor na matrix em cada laço de repetição da linha e coluna
print('=-'*30)

for l in range(0,3 ): #mesmo laço de cima  mas agora para printa valor
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix [l][c] %2 == 0:
            spar += matrix[l][c]
    print("")

print('=-'*30)


for l in range(0,3):
    scol += matrix[l][2]

for l in range(0,3):
    for c in range(0,3):
        maior = max(matrix[1])


print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {maior}')