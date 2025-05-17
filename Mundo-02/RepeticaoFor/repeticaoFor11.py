soma_idade = 0
contMulher20 = 0
pessoas = {}
maisVelho = ""
maiorIdade = 0
for i in range(1, 5):
    nome = str(input("Digite o nome da pessoa: ")).strip().title()
    idade = int(input("Digite a idade dela: "))
    sexo = str(input("Digite o sexo dela[M/F]: ")).strip().upper()

    soma_idade = soma_idade + idade
    if i == 1 and sexo == "M":
        maiorIdade = idade
        maisVelho = nome
    if sexo == "F" and idade < 20:
            contMulher20 += 1
    if sexo == "M" and idade > maiorIdade:
            maiorIdade = idade
            maisVelho = nome
media = soma_idade / 4
print("O homem mais velho possui {} anos e se chama {}\nHá {} mulheres menores de 20 anos\nA média de idade é {}".format(maiorIdade, maisVelho, contMulher20, media))
