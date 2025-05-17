from datetime import date

def voto(ano):
    if  18 > date.today().year - ano >= 16 or date.today().year - ano >= 70:
        return "OPCIONAL"
    elif date.today().year - ano >= 18:
        return "OBRIGATÓRIO"
    else:
        return "NEGADO"

anoNasc = int(input("Digite seu ano de nascimento: "))
print(f"Com {date.today().year - anoNasc} anos, o voto é: {voto(anoNasc)}")
