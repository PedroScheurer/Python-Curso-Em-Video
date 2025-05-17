vel = float(input("Velocidade do carro(km/h): "))
if vel > 80:
    print("Você foi multado")
    multa = (vel - 80) * 7
    print("Valor da multa: R${:.0f},00".format(multa))
else:
    print("Você não foi multado")