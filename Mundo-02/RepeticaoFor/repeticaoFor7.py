##verificar se é numero primo
def primo():
    tot = 0
    num = int(input("Digite um número para verificar se é primo: "))
    for i in range(1, num+1):
        if num % i == 0:
            tot += 1
            print("\033[33m", end="")
        else:
            print("\033[31m", end="")
        print("{} ". format(i), end="")
    print("\nO número {} é divisível {} vezes".format(num, tot))
    if tot == 2:
        print("E por isso ele É PRIMO")
    else:
        print("E por isso ele não é primo")
primo()
continuar = str(input("Deseja continuar?[S/N]")).strip().upper()
if continuar == "S":
    primo()
else:
    print("Obrigado por testar")