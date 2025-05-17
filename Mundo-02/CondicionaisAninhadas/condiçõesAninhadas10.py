#JOKENPÓ
import random
from time import sleep
maquina = random.randint(1,3)
print("Jogadas\n[1]Pedra\n[2]Papel\n[3]Tesoura")
"pedra" == 1
"papel" == 2
"tesoura" == 3
jogador = int(input("Escolha um: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("A maquina escolheu: {}".format(maquina))
print("VocÊ escolheu: {}".format(jogador))

if maquina == 1:
    if jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Você venceu")
    elif jogador == 3:
        print("Você perdeu")
    else:
        print("Jogada inválida")

if maquina == 2:
    if jogador == 1:
        print("Você perdeu")
    elif jogador == 2:
        print("Empate")
    elif jogador == 3:
        print("Você venceu")
    else:
        print("Jogada inválida")
if maquina == 3:
    if jogador == 1:
        print("Você venceu")
    elif jogador == 2:
        print("Você perdeu")
    elif jogador == 3:
        print("Empate")
    else:
        print("Jogada inválida")