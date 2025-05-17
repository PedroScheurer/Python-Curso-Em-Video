r1 = int(input("Digite o valor da primeira reta: "))
r2 = int(input("Digite o valor da segunda reta: "))
r3 = int(input("Digite o valor da segunda reta: "))

if abs(r2 - r3) < r1 < r2 + r3 or abs(r1 - r3) < r2 < r1 + r3 or abs(r1 - r2) < r3 < r1 + r2:
    print("Triângulo")
else:
    print("Não pode ser um triângulo")