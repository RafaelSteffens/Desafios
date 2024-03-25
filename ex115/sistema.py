from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'bd.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo...')
        break
    else:
        print('\033[31mERRO! Digite uma opção valido')
    sleep(2)