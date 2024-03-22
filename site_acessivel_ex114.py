from selenium import webdriver

try:
    navegador = webdriver.Chrome()
    navegador.get('https://www.google.com/')
    print('consegui')

except Exception as e:
    print('Não consegui')

    '''
    #Solução do professor
    import rllib
    import urllib.request

    try:
    site = urllib.request.urlopen('https://www.google.com')

except urllib.error.URLError:
    print('O site não esta disponivel')

else:
    print('Consegui acessar')


    '''