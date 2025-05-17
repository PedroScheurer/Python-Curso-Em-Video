from datetime import date
anoAtual = date.today().year
contMaior = 0
for p in range(1, 7 +1):
    anoNasc = int(input("Ano de nascimento: "))
    idade = abs(anoAtual - anoNasc)
    if idade  >= 18:
        is_maior = True
        contMaior += 1
        print(is_maior)
    else:
        is_maior = False
        print(is_maior)

print("{} pessoas são maiores de idade".format(contMaior))