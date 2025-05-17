numeros = []
pares = []
impares = []
while True:
    num = int(input("Digite um numero: "))
    numeros.append(num)
    opcao = str(input("Deseja continuar?[S/N] ")).upper()
    while opcao[0] not in "SN":
        opcao = str(int("Deseja continuar?[S/N] ")).upper()
    if opcao[0] in "N":
        break

for pos, i in enumerate(numeros):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"Lista completa: {numeros}.\nOs números pares são {pares}.\nOs números impares são {impares}.")
