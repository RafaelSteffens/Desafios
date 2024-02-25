login={'rafael':123, 'noeli':123}
print('''

[1] Já sou cadastrado
[2] Cadastrar

''')
opcao = int(input('Escolha uma opção! '))
print()

# USAR DEF PARA ORIENTAR A OBJETO

if opcao==1:
    
    nome = str(input("Digite o seu nome:   "))

    senha = int(input("Digite a sua senha:   "))
    
    if login [nome] == senha:
       print('Seja Bem Vindo{}'.format(login))
elif opcao==2:
    print('Digite seus dados aqui\n')
    cnome = str(input('Digite seu nome:  '))
    csenha = int(input('Digite a sua senha:  '))
    login [cnome] =csenha
    print(login)
    

print("|FIM!")