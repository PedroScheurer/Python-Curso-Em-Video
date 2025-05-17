matriz = []
valores = []
somap = somat = maiors = menors = 0

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
            somap += j
print(f"A soma dos valores pares é: {somap}")
for i in valores[2::3]:
    for j in i:
        somat += j
print(f"A soma dos valores da terceira coluna é: {somat}")
for i in valores[3:6]:
    for j in i:
        if i == 3:
            maiors = menors = j
        if maiors <= j:
            maiors = j

print(f"O maior valor da segunda linha é {maiors}")
