print("[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL")
opcao = int(input("Para qual operação deseja converter? "))
numeroConversao = int(input("Número que deseja converter: "))
numConvertido = numeroConversao

if opcao == 1:
    print("{} convertido em binário é {}.".format(numeroConversao, bin(numConvertido)[2:]))
elif opcao == 2:
    print("{} convertido em Octal é {}.".format(numeroConversao, oct(numConvertido)[2:]))
elif opcao == 3:
    print("{} convertido em Hexal é {}.".format(numeroConversao, hex(numConvertido)[2:]))
else:
    print("Opção inválida")