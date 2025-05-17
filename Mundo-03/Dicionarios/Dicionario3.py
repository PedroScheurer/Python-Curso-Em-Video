from random import randint
from time import sleep
from operator import itemgetter
remendo = 0
ranking = dict()
#sortear valores
jogadores = {"Jogador1" : randint(1,6),
             "Jogador2" : randint(1,6),
             "Jogador3" : randint(1,6),
             "Jogador4" : randint(1,6)
             }
#printar com sleep
for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    sleep(0.5)
print(f"\nRanking dos Jogadores: ")
#jogadores ordenados pelo numero do dado
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i in ranking:
    print(f"O {i[0]} tirou {i[1]} no dado")
    sleep(0.5)