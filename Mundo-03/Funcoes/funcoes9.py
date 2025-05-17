def ficha(name, gols = None):
    if len(name) == 0:
        name = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    return f"O jogador {name} fez {gols} gol(s) no campeonato"


n = str(input("Digite seu nome: "))
g = input("Número de gols: ")
print(ficha(n,g))