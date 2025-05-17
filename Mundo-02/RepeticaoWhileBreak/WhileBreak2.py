n = 0
while n >= 0:
    n = int(input("Digite um número para verificar sua tabuada: "))
    if n < 0:
        break
    for i in range(1,11):
        res = n * i
        print(f"{n} x {i} = {res}")
print("Finalizado")