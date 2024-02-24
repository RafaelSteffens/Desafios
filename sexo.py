while True:
    sexo = str(input("Digite o seu sexo: "))
    if sexo == 'm' or sexo == 'f':
        print("Sexo {} cadastrado com suceso".format(sexo))
        break
    else:
        print('digite novamente') 
    
print('final')