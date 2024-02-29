
principal=[[],[]]

for c in range(1,8):
    lista = (int(input(f'Digite o numero {c}: ')))
    if lista % 2 ==0:
        principal[0].append(lista)
        
    else:
        principal[1].append(lista)
        

principal[0].sort()
principal[1].sort()
print('=-'*30)
print(f'Os numeros pares são {principal[0]}\n E os numeros impares são {principal[1]}')

