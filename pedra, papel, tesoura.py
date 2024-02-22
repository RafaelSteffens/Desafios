import random
import time

#lista com opções do jogo
itens = ["pedra", "papel", "tesoura"]

#utiliza método random para computador escolher numero aleatório
computador = random.randint(0,2)


print("escolha a sua jogada: ")

#o for percorre a lista conferindo indice e itens da variavel itens
for i, item in enumerate (itens):
    print(f"{i}: {item}")

#jogador escolhe a jogada
jogador = int(input("Escolha a sua jogada: "))

time.sleep(0.5)
print("\n pedra, papel, tesoura.. \n")

print(f"você escolheu:  {itens[jogador]}")
print(f"o computador escolheu:  {itens[computador]}")


#lógica ganhador

if computador == jogador:
    print("empate")
elif (jogador ==0 and computador ==2 or jogador == 1 and computador == 0 or jogador ==2 and computador == 1):
    print("você ganhou")

else:
    print("você perdeu")

print("\n"+"="*33)





