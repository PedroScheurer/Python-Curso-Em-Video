numeros = []
for i in range(5):
    num = int(input(f"Digite o {i + 1} número: "))
    if i == 0:
        numeros.append(num)
        print(f"Adicionando valor na posição inicial")
    else:
        for j in range(len(numeros)):
            if num < numeros[j]:
                numeros.insert(j, num)
                print(f"Adicionando valor na posição {j + 1}")
                break
        else:
            numeros.append(num)
            print(f"Adicionando valor na posição final")
print(numeros)