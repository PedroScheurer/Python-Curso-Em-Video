abre_parenteses = fecha_parenteses = 0
expressao = str(input("Digite uma expressão: ")).strip().split()

for i in expressao:
    for j in i:
        if "(" in j:
            abre_parenteses += 1
        if ")" in j:
            fecha_parenteses += 1
if abre_parenteses == fecha_parenteses:
    print("Expressão válida")
else:
    print("Expressão inválida")