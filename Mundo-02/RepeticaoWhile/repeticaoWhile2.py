import random
erros = 1
num = random.randint(1,10)
tentativa = int(input("Tente acertar o número de 1 a 10: "))
while tentativa != num:
        if tentativa < num:
            print("O número é maior")
        else:
            print("O número é menor")
        erros += 1
        print("Número errado, tente novamente ")
        tentativa = int(input("Tente acertar o número de 1 a 10: "))
print("Número certo, você tentou {} vezes".format(erros))