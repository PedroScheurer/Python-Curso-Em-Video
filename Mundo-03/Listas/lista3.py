numeros = []
while True:
    num = int(input("Digite um número: "))
    if num not in numeros:
        print("Número adicionado")
        numeros.append(num)
    else:
        print("Número já está na lista, não vou adicionar")
    opcao = str(input("Deseja continuar?[S/N] ").upper())
    while opcao[0] not in "NS":
        opcao = str(input("Deseja continuar?[S/N] ").upper())
    if opcao[0] in "N":
        print("Finalizando...")
        break
numeros.sort()
print(f"Você digitou os valores: {numeros}")