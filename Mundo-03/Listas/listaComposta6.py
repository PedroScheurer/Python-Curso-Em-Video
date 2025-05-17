alunos = []
notas = []
nomes = []
medias = []
soma = mostraraluno = 0
#input ler nome
while True:
    nome = str(input("Nome: "))
    nomes.append(nome)
    # input ler notas
    for i in range(0,2):
        nota = int(input(f"Nota {i + 1}: "))
        #adicionar a lista de notas
        notas.append(nota)
    #adicionar infos a lista de alunos
    nomes.append(notas[:])
    alunos.append(nomes[:])
    notas.clear()
    nomes.clear()

    # input para opcao de continuar
    opcao = str(input("Deseja continuar?[S/N] ")).upper()
    while opcao[0] not in "SN":
        opcao = str(input("Deseja continuar? ")).upper()
    if opcao[0] == "N":
        break
print(f"{"=-"*20}")
#tirar media das notas de cada um
for pos, i in enumerate(alunos):
    for j in i[1]:
        soma += j
    media = soma/2
    medias.append(media)
    soma = 0
print(f"{"No.":<10}{"Nome":^10}{"Média":>10}\n{"-"*30}")
for pos, i in enumerate(alunos):
    print(f"{pos:<10}{i[0]:^10}{medias[pos]:>10}")
#input para mostar notas do aluno
while True:
    mostraraluno = int(input("Mostrar nota de qual aluno? [999 para interromper]: "))
    print(f"As notas de {alunos[mostraraluno][0]} são {alunos[mostraraluno][1]}")
    if mostraraluno == 999:
        print("FINALIZANDO...\nVolte Sempre")
        break