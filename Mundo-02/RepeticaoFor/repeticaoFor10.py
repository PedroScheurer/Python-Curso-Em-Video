#MEU JEITO
'''pesoPessoas = []
for p in range(1, 5+1):
    peso = float(input("Digite seu peso: "))
    pesoPessoas.append(peso)
print("O maior peso é de {}Kg.".format(max(pesoPessoas)))
print("O menor peso é de {}1Kg.".format(min(pesoPessoas)))'''

#JEITO DO GUANABARA
maiorPeso = 0
menorPeso = 0

for pes in range(1, 5+1):
    peso = float(input("Digite o peso da pessoa:"))
    if pes == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
            heavier = pes
        if peso < menorPeso:
            menorPeso = peso
            lighter = pes
print("O maior peso lido é {} da pessoa número {}.\nO menor peso lido é {} da pessoa número {}.".format(maiorPeso, heavier, menorPeso, lighter))