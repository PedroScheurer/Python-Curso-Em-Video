from random import randint
v = 0
while True:
    bot = randint(1, 11)
    player = int(input("Número de 1 a 10: "))
    opcao = str(input("Par ou Ímpar[P/I]: ")).upper().strip()
    while opcao not in "PI":
        opcao = str(input("Par ou Ímpar[P/I]: ")).upper().strip()
    print(f"Você jogou {player} e o computador {bot}")
    if (player + bot) % 2 == 0:
        is_par = True
        correto = "P"
    else:
        is_par = False
        correto = "I"
    if opcao == correto:
        print("Você venceu")
        v += 1
    else:
        break
print(f"Você venceu {v} vezes")
