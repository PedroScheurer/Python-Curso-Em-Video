def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {a}m2")


print(f"Controle de Terrenos\n{"-" *30}")
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)