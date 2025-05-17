from datetime import date
ano = int(input("Digite o ano que deseja verificar: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    is_bissexto = True
    print("{} é bissexto".format(ano))
else:
    is_bissexto = False
    print("{} não é bissexto".format(ano))