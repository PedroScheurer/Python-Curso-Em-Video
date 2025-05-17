jogador = dict()
gols = list()
tot = 0
nome = str(input("Nome do jogador: "))
qntdJogos = int(input("Quantidade de partidas jogadas: "))
jogador["nome"] = nome
jogador["qntdJogos"] = qntdJogos
print(f"{"-="*30}")
for i in range(jogador["qntdJogos"]):
    gol = int(input(f"Quantos gols na partida {i}: "))
    tot += gol
    gols.append(gol)
jogador["gols"] = gols[:]
jogador["totalGols"] = tot
print(f"{"-="*30}")
for k, v in jogador.items():
    print(f"O {k} é {v}")
print(f"{"-="*30}")
print(f"O jogador {jogador["nome"]} jogou {jogador["qntdJogos"]} jogos.")
for i in range(jogador["qntdJogos"]):
    print(f"Na partida {i + 1}, o jogador fez {jogador["gols"][i]} gols.")