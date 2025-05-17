matriz = []
valores = []
pares = []
for i in range(3):
    for j in range(3):
        num = int(input(f"Digite o valor para [{i + 1}, {j + 1}]: "))
        matriz.append(num)
        valores.append(matriz[:])
        matriz.clear()
print(f"{valores[:3]}")
print(f"{valores[3:6]}")
print(f"{valores[6:9]}")
for i in valores:
    for j in i:
        if j % 2 == 0:
            pares.append(j)
    
