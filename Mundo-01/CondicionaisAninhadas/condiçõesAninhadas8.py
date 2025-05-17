altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)
print("{:.1f}".format(imc))

if imc <= 18.5:
    print("Abaixo do Normal")
elif 18.5 < imc <= 24.9:
    print("Normal!")
elif 25 < imc <= 29.9:
    print("Sobrepeso")
elif 30 < imc <= 34.9:
    print("Obesidade grau I")
elif 35 < imc <= 39.9:
    print("Obesidade grau II")
elif imc >= 40:
    print("Obesidade grau III")