valores = []
pares = []
impares = []
for i in range(0,7):
    num = int(input("Digite um valor: "))
    valores.append(num)
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
valores.clear()
pares.sort()
impares.sort()
valores.append(pares[:])
valores.append(impares[:])
print(f"Valores pares: {pares}\nValores impares: {impares}")
