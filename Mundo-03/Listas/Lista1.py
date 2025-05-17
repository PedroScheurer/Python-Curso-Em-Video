lista = ["pizza", "hamburguer", "cachorro quente"]

lista.append("suco")
lista.insert(0, "massa")
print(lista)

del lista[3]
lista.pop()
lista.remove("hamburguer")
if "pizza" in lista:
    lista.remove("pizza")

print(lista)

valores = [7, 2, 5, 6, 3, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
for c in range(0,3):
    valores.append(int(input("Digite um valor: ")))
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}.")
print("Cheguei ao final")

a = [1, 2 ,3]
#cria uma ligação
b = a
#cria uma copia com os elementos de A
b = a[:]
b.append(4)

print(a)
print(b)
