maior = menor = h = m = menos20 = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo[M/F]: ")).strip()
    if idade >= 18:
        maior += 1
    else:
        menor += 1
    if sexo[0] in "Mm":
        h += 1
    elif sexo[0] in "Ff":
        m += 1
        if idade < 20:
            menos20 += 1
    opcao = str(input("Deseja continuar[S/N]? ")).strip()
    while opcao not in "SsNn":
        opcao = str(input("Deseja continuar[S/N]? ")).strip().upper()
    if opcao in "Nn":
        break
print(f"{maior} maiores de idade.\nPossuem {h} homens e {m} mulheres.\nE {menos20} são mulher com menos de 20 anos.")