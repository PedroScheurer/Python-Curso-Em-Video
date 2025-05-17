from operator import index

jogador = dict()
jogadores = list()
gols = list()
tot = cod = 0
while True:
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
    jogador["Cod"] = cod
    cod += 1
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    tot = 0
    opcao = str(input("Deseja continuar[S/N]? ")).upper()
    if opcao[0] not in "SN":
        opcao = str(input("Deseja continuar[S/N]? ")).upper()
    if opcao[0] == "N":
        break
print(f"{"-="*30}")
print(f"{"Cod":<10}{"Nome":^10}{"Gols":^15}{"Total de Gols":>15}")
print(f"{"-="*30}")
for i in jogadores:
    print(f"{i["Cod"]:<10}{i["nome"]:^10}{str(i["gols"]):^15}{i["totalGols"]:>15}")
print(f"{"-="*30}")
while True:
    opcAluno = int(input("Qual aluno deseja mostrar[999 para cancelar]? "))
    if 999 > opcAluno > len(jogadores):
        print("Invalido")
        opcAluno = int(input("Qual aluno deseja mostrar? "))
    if opcAluno == 999:
        print("Finalizando")
        break
    for i in jogadores:
        if opcAluno == i["Cod"]:
            for pos, v in enumerate(i["gols"]):
                print(f"No jogo {pos} ele marcou {v} gols.")

