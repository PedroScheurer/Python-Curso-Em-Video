num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("[1]Soma\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa")
opcao = int(input("Escolha uma opção: "))
while opcao != 5:
    if opcao == 1:
        resultado = num1 + num2
        print("{} + {} = {}".format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print("{} x {} = {}".format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            maiorNum = num1
        elif num1 < num2:
            maiorNum = num2
        else:
            maiorNum = None
        print("{} é o maior".format(maiorNum))
    elif opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print("[1]Soma\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa")
    opcao = int(input("Escolha uma opção: "))
print("Obrigado por participar")
