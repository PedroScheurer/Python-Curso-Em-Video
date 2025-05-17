from random import randint
from time import sleep
jogos = []
jogo = []
#perguntar quantos jogos deseja gerar e fazer loop
print(f"{"="*30}\n{"JOGA NA MEGA SENA".center(30)}\n{"="*30}")
qntdJogos = int(input("Quantos jogos deseja gerar? "))
remendo = qntdJogos
while qntdJogos != 0:
#sortear 6 numeros de 1 a 60
    for i in range(0, 6):
        while True:
            num = randint(1, 61)
#não podem se repetir dentro de um mesmo jogo
            if num not in jogo:
                jogo.append(num)
                break
#armazenar numa lista
    jogos.append(jogo[:])
    jogo.clear()
    qntdJogos -= 1
print(f"{"-="*3}{" SORTEANDO "}{remendo}{" JOGOS "}{"-="*3}")
for i in jogos:
    print(sorted(i))
    sleep(0.7)
print(f"{"-="*5}{" BOA SORTE! "}{"-="*5}")