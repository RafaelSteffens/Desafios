'''
from random import *
import os
u_pwd = input ("Digite uma senha: ")
pwd = {'a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','z','y','w','1','2','3','4','5','6','7','8','9'}



pw=""

while (pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,32)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Estamos descobrindo a sua senha...")
        os.system('cls')

print(f"A senha craqueada é: {pw}")
'''
# Importando os módulos necessários
import random
import os
import time

# Definindo uma lista com as possíveis letras da senha
pwd = 'abcdefghijlmnopqrstuvwxyz123456789'

# Pedindo ao usuário que digite uma senha
u_pwd = input("Digite uma senha: ")

# Iniciando uma variável para armazenar a senha adivinhada
pw = ""

# Iniciando uma variável para contar o número de tentativas
tentativas = 0

# Iniciando uma variável para medir o tempo de execução
inicio = time.time()

# Criando uma função para limpar a tela de acordo com o sistema operacional
def clear():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux ou Mac
        os.system('clear')

# Criando um loop enquanto a senha adivinhada for diferente da senha do usuário
while pw != u_pwd:
    # Limpando a tela
    clear()
    # Gerando uma senha aleatória com o mesmo tamanho da senha do usuário
    pw = "".join(random.choices(pwd, k=len(u_pwd)))
    # Imprimindo a senha adivinhada
    print(pw)
    # Imprimindo uma mensagem de progresso
    print("Estamos descobrindo a sua senha...")
    # Incrementando o número de tentativas
    tentativas += 1

# Calculando o tempo de execução
fim = time.time()
duracao = fim - inicio

# Imprimindo a senha craqueada, o número de tentativas e o tempo de execução
print(f"A senha craqueada é: {pw}")
print(f"Número de tentativas: {tentativas}")
print(f"Tempo de execução: {duracao:.2f} segundos")

'''
#teste3
import random
import time
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def generate_random_password(length):
    characters = 'abcdefghijlmnopqrstuvwxyz123456789'
    return ''.join(random.choices(characters, k=length))

def main():
    user_password = input("Digite uma senha: ")
    guessed_password = ""
    attempts = 0
    start_time = time.time()

    while guessed_password != user_password:
        clear_screen()
        guessed_password = generate_random_password(len(user_password))
        print(guessed_password)
        print("Estamos descobrindo a sua senha...")
        attempts += 1

    end_time = time.time()
    duration = end_time - start_time

    print(f"A senha craqueada é: {guessed_password}")
    print(f"Número de tentativas: {attempts}")
    print(f"Tempo de execução: {duration:.2f} segundos")

if __name__ == "__main__":
    main()


'''
