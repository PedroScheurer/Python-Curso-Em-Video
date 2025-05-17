valores = (int(input("Valor 1: ")), int(input("Valor 2: ")),
           int(input("Valor 3: ")), int(input("Valor 4: ")))
print(valores)
c9 = 0
tres = False
for i in valores:
    while i == 3:
        pos3 = valores.index(i)
        tres = True
        break
    if i % 2 == 0:
        print(f"O valor {i} é par")
qntd9 = valores.count(9)
print(f"O valor 9 aparece {qntd9} vezes.")
if tres == False:
    print("O valor 3 não foi digitado")
else:
    print(f"O valor 3 aparece pela primeira vez na posição {pos3 + 1}")