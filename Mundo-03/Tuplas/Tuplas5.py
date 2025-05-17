lista = ("mouse", 50, "placa de vídeo", 2500, "teclado", 200)
texto = "Listagem de preços"
print("-" * 30)
print(f"{texto: ^30}")
print("-" * 30)
for i in range(0, len(lista), 2):
    produto = lista[i]
    valor = lista[i + 1]
    print(f"{produto:.<30}R${valor:.2f}")
print("-" * 30)