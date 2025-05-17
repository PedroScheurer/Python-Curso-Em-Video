from time import sleep
def contador():
    print(f"{"-" * 30}")
    print(f"Contagem de 1 até 10 de 1 em 1")
    for i in range(1, 11):
        print(i, end=" ")
        sleep(0.3)
    print(f"\n{"-"*30}")
    print(f"Contagem de 10 até 0 de 2 em 2")
    for i in range(10, 0, -2):
        print(i, end=" ")
        sleep(0.3)
    print(f"\n{"-" * 30}")
    print("Agora é sua vez de personalizar a contagem!")
    a = int(input("Inicio = "))
    b = int(input("Fim = "))
    c = int(input("Passo = "))
    print(f"Contagem de {a} até {b} de {c} em {c}")
    if c == 0:
        c = -1
    if b > a:
        b += 1
    if a > b:
        b -= 1
    if c > 0 and a > b:
        c *= -1
    for i in range(a, b, c):
        print(i, end=" ")
        sleep(0.3)


contador()