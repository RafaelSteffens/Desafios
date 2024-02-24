valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite um valor: "))

def somar():
    return valor1 + valor2

def multiplica():
    return valor1 * valor2

def maior():
    return max(valor1, valor2)

while True:
    print("""
    Escolha no menu
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos valores
        [5] sair programa
    """)
    escolha = int(input('Digite 1 a 5 para escolher a opção: '))

    if escolha == 1:
        print('\n A soma é:', somar())  # Corrigido: chamando a função somar()

    elif escolha == 2:
        print('\n A multiplicação é:', multiplica())

    elif escolha == 3:
        print('\n O maior número é', maior())

    elif escolha == 4:
        print('\n Reiniciando programa')
        break
    elif escolha == 5:
        break

print('FIM')