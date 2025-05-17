from random import randint
from time import sleep

def sorteia(lista):
    for i in range(0,5):
        lista.append(randint(1,100))
    print(f"Sorteando 5 valores da lista: ", end="")
    for i in numeros:
        sleep(0.3)
        print(i, end=" ")

numeros = list()

def somaPar():
    sleep(1)
    print("\nSomando números pares...")
    sleep(1)
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    print(f"A soma entre os valores {numeros} foi {s}")
    numeros.clear()

sorteia(numeros)
somaPar()
sorteia(numeros)
somaPar()
sorteia(numeros )
somaPar()