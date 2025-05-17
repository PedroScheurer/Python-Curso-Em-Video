r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da segunda reta: "))

if abs(r2 - r3) < r1 < (r2 + r3) or abs(r1 - r3) < r2 < (r1 + r3) or abs(r1 - r2) < r3 < (r1 + r2):
    print("Triângulo")
    is_triangulo = True
else:
    print("Não pode ser um triângulo")
    is_triangulo = False
if is_triangulo == True:
    if r1 == r2 == r3:
      print("Equilátero")
    elif r1 != r2 != r3 != r1:
     print("Escaleno")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Isósceles")