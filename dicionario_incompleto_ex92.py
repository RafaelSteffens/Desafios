from datetime import datetime
cadastro = {}

while True:
    nome = str(input("Nome: "))
    cadastro['nome'] = nome
    ano_nascimento = int(input("Ano de nascimento: "))
    cadastro["nasc"] = ano_nascimento
    ctps = int(input("Carteira de Trabalho: (0 não tem) "))
    cadastro["ctps"] = ctps
    if ctps == 0:
        print("finalizandooo...")
        print("=-"*30)
        print(cadastro)
        idade = (datetime.now().year - (cadastro["nasc"]))
        print(f"\nNome tem o valor {cadastro['nome']}")
        print(f'Idade tem o valor {idade}')
        print(f'Ctps tem o valor {cadastro["ctps"]}')



        break
    else:
        contratacao = int(input("Ano de Contratação: "))
        cadastro["contratacao"] = contratacao
        salario = float(input("Salário: R$ "))
        cadastro["salario"] = salario
        
        idade = (datetime.now().year - (cadastro["nasc"]))
        cont = (cadastro["contratacao"])
        aposentadoria = (((cont)+35)-2024)

        print("=-"*30)
        print(cadastro)
        print(f"\nNome tem o valor {cadastro['nome']}")
        print(f'Idade tem o valor {idade}')
        print(f'Ctps tem o valor {cadastro["ctps"]}')
        print(f'Contratação tem o valor {cadastro["contratacao"]}')
        print(f'Salario tem o valor R$ {cadastro["salario"]:2f}')
        print(f' E ele vai se aposentar aos {aposentadoria} anos')
        break


