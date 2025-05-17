pessoa = dict()
pessoas = list()
somaIdade = 0
mulheres = list()
maioresMedia = list()
while True:
    nome = str(input("Nome: "))
    sexo = str(input("Sexo: "))
    idade = int(input("Idade: "))
    pessoa["nome"] = nome
    pessoa["sexo"] = sexo
    pessoa["idade"] = idade
    pessoas.append(pessoa.copy())
    pessoa.clear()

    opcao = str(input("Deseja continuar[S/N]? ")).upper()
    if opcao[0] not in "SN":
        opcao = str(input("Deseja continuar[S/N]? ")).upper()
    if opcao[0] == "N":
        break
print(f"Foram cadastradas {len(pessoas)} pessoas.")
for i in pessoas:
    somaIdade += i["idade"]
    if i["sexo"][0] in "Ff":
        mulheres.append(i)
media = somaIdade/len(pessoas)
for i in pessoas:
    if i["idade"] > media:
        maioresMedia.append(i)
print(f"A media das idades é {media}")
print(f"As mulheres são: {mulheres}")
print(f"Os que possuem idade maior que a média são {maioresMedia}")