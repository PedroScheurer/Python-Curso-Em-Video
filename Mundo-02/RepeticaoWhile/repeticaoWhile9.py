opcao = ""
qntN = 0
soma = 0
while opcao != "N":
    num = int(input("Digite um número: "))
    if qntN == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    qntN += 1
    soma += num
    opcao = str(input("Deseja continuar?[S/N]: ")).upper().strip()
    if opcao not in "SsNn":
        print("Opção inválida")
        break
media = soma / qntN
print("A media entre os números é {}.\nO maior é {} e o menor é {}.".format(media, maior, menor))