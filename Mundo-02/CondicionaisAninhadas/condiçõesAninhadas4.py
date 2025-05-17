from datetime import date
anoNasc = int(input("Digite o seu ano de nascimento: "))
dataAtual = date.today()
idade = dataAtual.year - anoNasc

print("Sua idade é {}".format(idade))

if idade < 18:
    prazo = abs(idade - 18)
    print("Sua idade é menor que 18, ainda terá que se alistar.\nFaltam {} anos para se alistar.".format(prazo))
    anoAlist = prazo + dataAtual.year
    print("Seu alistamento será em {}".format(anoAlist))
elif idade == 18:
    print("Chegou aos 18, aliste-se já!")
elif idade > 18:
    prazo = abs(idade - 18)
    print("Seu prazo de alistatemento passou. Caso não tenha-se alistado ainda, apresente-se na Junta de Serviço.\nFazem {} ano(s) de seu alistamento".format(prazo))
    anoAlist = dataAtual.year - prazo