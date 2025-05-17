total = maiormil = barato = 0
pbarato = ""
while True:
    nome = str(input("Nome do produto: "))
    preco = int(input("Preço do produto: R$"))
    if total == 0:
        barato = preco
        pbarato = nome
    if barato > preco:
        barato = preco
        pbarato = nome
    total += preco
    if preco > 1000:
        maiormil += 1
    opcao = str(input("Deseja continuar[S/N]? ")).strip()
    while opcao not in "SsNn":
        opcao = str(input("Deseja continuar[S/N]? ")).strip()
    if opcao in "Nn":
        break
print(f"Total = {total}\nValores maiores que mil = {maiormil}\nO produto mais barato é o {pbarato} custando R${barato}")