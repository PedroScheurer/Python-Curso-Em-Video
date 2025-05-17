
lista = []

for v in range(0,5):
    num = (int(input("Digite um valor: ")))
    lista.append(num)
print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} na(s) posição ", end=" ")
for pos, i in enumerate(lista):
    if max(lista) == i:
        print(pos + 1, end= "...")
print(f"\nO menor valor digitado foi {min(lista)} na(s) posição ", end="")
for pos, i in enumerate(lista):
    if min(lista) == i:
        print(pos + 1, end="...")