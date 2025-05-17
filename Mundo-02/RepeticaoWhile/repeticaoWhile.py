sexo = ""
sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()
while sexo != "M" and "F":
    sexo = str(input("Valor inválido, tente novamente: ")).upper().strip()
print("Sexo {} escolhido".format(sexo))