dict = {}
list=[]
aprov = 0
for c in range(1):
    nome = str(input('Digite o nome: '))
    media = int(input('Digite a média: '))
    dict['nome']= nome
    dict['media']= media
    list.append(dict)
    del dict
    
#nome = dict[0].values()
'''
for n, m in dict.items():
    print(f'no n tem {n} e nom tem {m}')
'''
print(dict)
nome =(list[0]['nome'])
media = (list[0]['media'])
print(f'O nome é {nome}', end=" ")
print(f'a média é {media}')

if media >= 7:
        print('Situação igual a aprovado')

else:
      print('Aluno reprovado')




    
    
