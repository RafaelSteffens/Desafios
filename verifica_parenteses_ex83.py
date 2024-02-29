var = str(input('Digite uma expressão: '))
def verifica(string):
    lista=[]
    for  char in string:
        if char == "(":
            lista.append(char)

        elif char == ")":
            if not lista:
                return False
            
            lista.pop()
    return len(lista) == 0
 
resultado = verifica(var)

if resultado:
    print('A expressão está correta')

else:
    print('A expree~soa está aberta')