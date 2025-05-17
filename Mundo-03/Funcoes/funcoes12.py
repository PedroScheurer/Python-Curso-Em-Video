while True:
    opcao = str(input("Função ou Biblioteca: "))
    if opcao == "fim":
        break
    else:
        print(f"\033[42m\033[97m{"="*30}\nAcessando o manual do comando '{opcao}'\n{"="*30}\033[0m")
        print("\033[41m\033[97m")
        help(opcao)
        print("\033[0m")
print(f"\033[44m\033[97m{"="*10}\nATÉ LOGO\n{"="*10}\033[0m")