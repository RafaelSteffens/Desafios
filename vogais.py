def mostra_vogais(palavra):
    vogais = 'aeiouAEIOU'
    vogais_encontradas = [letra for letra in palavra if letra in vogais]
    return vogais_encontradas

# Tupla de palavras
tuplas = ("aprender", "programar", "python", "milionario")

# Iterando pelas palavras na tupla
for palavra in tuplas:
    vogais_na_palavra = mostra_vogais(palavra)
    if vogais_na_palavra:
        print(f"Na palavra '{palavra}' tem as seguintes vogais: {', '.join(vogais_na_palavra)}")
    else:
        print(f"A palavra '{palavra}' não possui vogais.")

print('FIM')
