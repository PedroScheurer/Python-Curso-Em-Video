numeros = []
while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    opcao = str(input("Deseja continuar?[S/N] ")).upper().strip()
    while opcao not in "SN":
        print("Opção inválida")
        opcao = str(input("Deseja continuar?[S/N] ")).upper().strip()
    if opcao[0] == "N":
        break
print(f"Foram digitados {len(numeros)} numeros.")
numeros.sort(reverse=True)
print(f"Lista de numeros invertida: {numeros}")
numeros.sort(reverse=False)
print(f"Lista de numeros normal: {numeros}")
for pos, i in enumerate(numeros):
    if 5 == i:
        print(f"O número 5 está na lista na posição {pos + 1}.")