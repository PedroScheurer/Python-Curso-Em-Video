pessoa = []
pessoas = []
pesos = []
pesados = []
leves = []
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])
    pessoa.clear()
    opcao = str(input("Deseja continuar?[S/N] ")).upper()
    if opcao[0] not in "SN":
        opcao = str(input("Deseja continuar?[S/N] ")).upper()
    if opcao[0] in "N":
        break
print(f"Existem {len(pessoas)} pessoas na lista")
for i in range(len(pessoas)):
    pesos.append(pessoas[i][1])
print(f"O maior peso é {max(pesos)}. Peso(s) de ",end="")
for pos, i in enumerate(pesos):
    if i == max(pesos):
        pesados.append(pessoas[pos][0])
    elif i == min(pesos):
        leves.append((pessoas[pos][0]))
print(pesados)
print(f"O menor peso é {min(pesos)}. Peso(s) de ",end="")
print(leves)
