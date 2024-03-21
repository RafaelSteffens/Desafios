def leiaInt ( a ):
    while True:
        try:
            n = int(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return n

def leiaFloat (a):
    while True:
        try:
            n = float(input(a))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro foi {n1} e o real foi {n2}')