from datetime import date
anoNasc = int(input("Ano de nascimento: "))
dataAtual = date.today()
idade = abs(anoNasc - dataAtual.year)

if idade <= 9:
    print("Mirim")
elif idade <= 14 and idade > 9:
    print("Infantil")
elif idade <= 19 and idade > 14:
    print("Junior")
elif idade <= 25:
    print("Sênior")
elif idade > 25:
    print("Master")