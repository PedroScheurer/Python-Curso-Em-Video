import random
from time import sleep
numAleatorio = random.randint(0, 5)

tentativas = 1
while tentativas <= 3:
    numInput = int(input("Digite um número de 0 a 5: "))
    print("Processando...")
    sleep(2)
    if numInput > 5:
        print("Número inválido")
    elif numInput == numAleatorio:
        print("Você acertou!")
        break
    else:
       print("Você errou")
       print("{} vida(s) usada(s), faltam {} tentativa(s)".format(tentativas, abs(tentativas-3)))
       tentativas = tentativas + 1